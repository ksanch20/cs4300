import sys, os, pytest

#Import task6 functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task6 import count_words_in_file

#Verify that count_words_in_file returns correct amount of words in task6_read_me 
def test_count_words_in_file():
    assert count_words_in_file("/home/student/cs4300/homework1/task6_read_me.txt") == 127

#Same test as above but parametrized 

@pytest.mark.parametrize(
    "filepath, expected_count",
    [
        ("/home/student/cs4300/homework1/task6_read_me.txt", 127),
    ],
)

def test_count_words_in_file_2(filepath, expected_count):
    assert count_words_in_file(filepath) == expected_count