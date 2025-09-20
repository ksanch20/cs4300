import sys, os

#Import task6 functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task6 import count_words_in_file

#Verify that count_words_in_file returns correct amount of words in task6_read_me 
def test_count_words_in_file():
    assert count_words_in_file("/home/student/cs4300/homework1/task6_read_me.txt") == 127
