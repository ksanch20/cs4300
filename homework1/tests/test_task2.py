import sys, os

#Import task2 functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task2 import Bool, Float, String, Int

#Test that Bool() returns a boolean 
def test_bool():
    assert isinstance(Bool(),bool)

#Test that Int() returns an integer
def test_int():
    assert isinstance(Int(),int)

#Test that String() returns a string
def test_string():
    assert isinstance(String(), str)

#Test that Float() returns a float 
def test_float():
    assert isinstance(Float(),float)