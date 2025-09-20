import sys, os

#Import task7 functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task7 import find_mean

#Verify find_mean finds correct mean 
def test_find_mean():
    assert find_mean([1,2,3,4]) == 2.5
    assert find_mean([10,20,60]) == 30