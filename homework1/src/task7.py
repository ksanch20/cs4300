#import numpy
import numpy as np 

#Function to find mean of list of numbers 
def find_mean(numbers):
    #create array 
    arr=np.array(numbers)
    #calculate mean using np 
    mean = float(np.mean(arr))
    #print mean 
    print(mean)
    #return mean
    return mean

#find_mean([1,2,3,4])