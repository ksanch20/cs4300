import sys, os

#Import task5 functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task5 import list_of_books, student_database

#Verify that list_of_books outputs first 3 books in list 
def test_list_of_books():
    assert list_of_books() == [{'title': "Since You've Been Gone", 'author': 'Morgan Matson'}, {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde'}, {'title': 'I Was Here', 'author': 'Gayle Forman'}]

#Verify 3 books are returned 
def test_list_of_books_length():
    result = list_of_books()
    assert len(result) == 3

#Verify that output of task5.py is first 3 books from list 
def test_list_of_books_output(capsys):
	list_of_books()
	captured = capsys.readouterr()
	assert captured.out.strip() == str([
        {"title": "Since You've Been Gone", "author": "Morgan Matson"},
        {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
        {"title": "I Was Here", "author": "Gayle Forman"}
    ])

#Verify that student_database returns dictionary with student names and ids
def test_student_database():
    assert student_database() == {'Kylie': 'S1', 'John': 'S2', 'Caroline': 'S3'}

# Ensure return type is a dictionary
def test_student_database_type():
    students = student_database()
    assert isinstance(students, dict)

# Ensure keys exist
def test_student_database_keys():
    students = student_database()
    assert "Kylie" in students
    assert "John" in students
    assert "Caroline" in students

