import sys, os

#Import task3 functions 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task3 import check_sign, sum_nums, first_10_primes

#Verify that check_sign returns "Negative" when arg is negative
def test_negative():
    assert check_sign(-1) == "Negative"

#Verify that check_sign returns "Positive" when arg is positive
def test_positive():
    assert check_sign(1) == "Positive"

#Verify that check_sign returns "Zero" when arg is zero
def test_zero():
    assert check_sign(0) == "Zero"

#Verify that test_sum returns the sum of 1 to 100 (5050)
def test_sum():
    assert sum_nums() == 5050

#Verify that test_first_10_primes returns first ten prime numbers 
def test_first_10_primes():
    assert first_10_primes() == [2,3,5,7,11,13,17,19,23,29]
