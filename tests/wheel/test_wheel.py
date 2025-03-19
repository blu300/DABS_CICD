import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../.."))  # Go up two levels
IMPORT_PATH = os.path.join(PROJECT_ROOT, "src")

sys.path.insert(0, IMPORT_PATH )

import my_wheel.my_module as my  

def test_add_two_numbers():
    assert my.add_two_numbers(9, 1) == 10

test_add_two_numbers()
