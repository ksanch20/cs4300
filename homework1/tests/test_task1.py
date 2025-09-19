import sys, os

#Import task1 function
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task1 import print_hello_world

#Verify that output of task1.py is "Hello, world!"
def test_print_hello_world(capsys):
	print_hello_world()
	captured = capsys.readouterr()
	assert captured.out.strip() == "Hello, world!"
