from my_wheel.my_module import *

def main():

  first = 310
  second = 400

  print(f"{first} + {second} = {add_two_numbers(first, second)}")
  print(f"{second} - {first} = {subtract_two_numbers(second, first)}")
  print(f"{first} * {second} = {multiply_two_numbers(first, second)}")
  print(f"{second} / {first} = {divide_two_numbers(second, first)}")

if __name__ == "__main__":
  main()