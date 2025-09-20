#Function to count words in a file 
def count_words_in_file(filename):
    #Open file for reading 
    with open(filename,"r") as file:

        #read from file
        text=file.read()

        #split string into substrings, removing spaces 
        words=text.split()

        #print amount of words 
        print(len(words))

        #return amount of words
        return len(words)

#count_words_in_file("/home/student/cs4300/homework1/task6_read_me.txt")