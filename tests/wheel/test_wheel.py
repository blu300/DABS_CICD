import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

import my_wheel.my_module as my  

def test_add_two_numbers():
    assert my.add_two_numbers(9, 1) == 10

test_add_two_numbers()
