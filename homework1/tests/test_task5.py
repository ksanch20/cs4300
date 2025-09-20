import sys, os

#Import task5 functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task5 import list_of_books, student_database

#Verify that list_of_books outputs first 3 books in list 
def test_list_of_books():
    assert list_of_books() == [{'title': "Since You've Been Gone", 'author': 'Morgan Matson'}, {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde'}, {'title': 'I Was Here', 'author': 'Gayle Forman'}]

#Verify that student_database returns dictionary with student names and ids
def test_student_database():
    assert student_database() == {'Kylie': 'S1', 'John': 'S2', 'Caroline': 'S3'}