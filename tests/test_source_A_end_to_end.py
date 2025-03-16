# Databricks notebook source

pip install nutter

# COMMAND ----------

# DBTITLE 1,Imports
from runtime.nutterfixture import NutterFixture, tag
import random
from pyspark.testing import assertDataFrameEqual

# COMMAND ----------

# DBTITLE 1,Test Data (input)
test_data = [
        ("1", "foo", "a", "x"),  
        ("2", "bar", "b", "y"),
        ("3", "baz", "c", "z")]

test_schema =["col_1", "col_2", "col_3", "col_4"]

test_df = df = spark.createDataFrame(test_data, test_schema)

# COMMAND ----------

# DBTITLE 1,Expected data (output)
expected_data = [
        ("11111111", "foofoofoofoofoofoofoofoo", "aaaaaaaa", "xxxxxxxx"),  
        ("22222222", "barbarbarbarbarbarbarbar", "bbbbbbbb", "yyyyyyyy"),
        ("33333333", "bazbazbazbazbazbazbazbaz", "cccccccc", "zzzzzzzz")]

expected_schema =["col_1", "col_2", "col_3", "col_4"]

expected_df = df = spark.createDataFrame(expected_data, expected_schema)

# COMMAND ----------

# create unique test-identifier to be used as prefix 
# for tables created during test
test_identifier = random.randint(0,1000)

#define variables that are to be used/passed during test
layers = ["raw", "bronze", "silver", "gold"]
table_name_dict = {layer: f"{layer}.source_a.{test_identifier}_{layer}_table" 
                   for layer in layers}

#construct argument dict to pass to dbutils.notebook.run
bronze_args = {"source_table": table_name_dict["raw"],
               "destination_table": table_name_dict["bronze"]}

silver_args = {"source_table": table_name_dict["bronze"],
               "destination_table": table_name_dict["silver"]}

gold_args = {"source_table": table_name_dict["silver"],
             "destination_table": table_name_dict["gold"]}

# COMMAND ----------

class MyTestFixture(NutterFixture):

   def before_source_a_end_to_end(self):
      print(test_identifier)

      #create raw data table using test data
      test_df.write.saveAsTable(table_name_dict["raw"])

   def run_source_a_end_to_end(self):
      (dbutils.notebook
       .run('./source_A_1_raw_to_bronze_notebook', 600, bronze_args))
      (dbutils.notebook
       .run('./source_A_2_bronze_to_silver_notebook', 600, silver_args))
      (dbutils.notebook
       .run('./source_A_3_silver_to_gold_notebook', 600, gold_args))

   def assertion_source_a_end_to_end(self):
      output_df = spark.read.table(table_name_dict["gold"])
      assertDataFrameEqual(expected_df, output_df)

   def after_source_a_end_to_end(self):
      [spark.sql(f"DROP TABLE {table_name_dict[layer]}") for layer in layers]

result = MyTestFixture().execute_tests()
print(result.to_string())
# Comment out the next line (result.exit(dbutils)) 
# to see the test result report from within the notebook
result.exit(dbutils)
