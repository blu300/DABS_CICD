# Databricks notebook source
import pyspark.sql.functions as F

# COMMAND ----------

source_table_name= dbutils.widgets.get("source_table")
destination_table_name = dbutils.widgets.get("destination_table")

# COMMAND ----------

source_df = spark.read.table(source_table_name)
for column in source_df.columns:
    processed_df = source_df.withColumn(column, F.repeat(column,2))
    source_df = processed_df
processed_df = processed_df.sort(F.col("col_1").asc())

# COMMAND ----------

processed_df.write.mode("overwrite").saveAsTable(destination_table_name)
