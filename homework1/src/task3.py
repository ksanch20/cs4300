#Function to test if a number is positive negative or 0
def check_sign(num):

    #If number is less than zero return "Negative"
    if (num < 0):
        return "Negative"

    #If number equals zero return "Zero"
    elif (num == 0):
       return "Zero"

    #Else return "Positive"
    else:
        return "Positive"

def first_10_primes():

    #Create list to hold prime numbers
    primes = []
    
    #start checking from 2
    num=2 

    #While there are less than 10 prime numbers in list 
    while len(primes) < 10: 
        #check if num is prime 
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False 
                break
        if is_prime:
            primes.append(num)
        num+=1

    #print prime numbers
    for prime in primes:
        print(prime)

    #return list of first 10 prime numbers 
    return primes
                       



#Function to get sum of numbers from 1 to 100
def sum_nums():

    #total variable to keep track of sum
    total=0
    i=1

    #While loop to add from 1 to 100
    while i<= 100:
        total+= i
        i+=1

    #Return total sum
    return total



