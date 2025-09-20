#Function that prints first three books in list of books 
def list_of_books():
    #initialize list of books and authors 
    books =[
       { "title": "Since You've Been Gone", "author": "Morgan Matson" },
       { "title": "The Picture of Dorian Gray", "author": "Oscar Wilde" },
       { "title": "I Was Here", "author": "Gayle Forman" },
       { "title": "We Were Liars", "author": "E. Lockhart" },
    ]

    #Slice first three books 
    first_3=books[:3]
    #print first three books 
    print(first_3)
    #return first three books 
    return first_3

#Function to print dictionary with students names and ids
def student_database():
    students = {
        "Kylie": "S1",
        "John": "S2",
        "Caroline": "S3",
    }
    print(students)
    return students

#list_of_books()
#student_database()