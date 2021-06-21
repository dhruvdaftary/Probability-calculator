#It might not work for larger values, in that case use google colab GPU
import sys
sys.setrecursionlimit(10**6) #For increasing the factorial limit
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

def combination(a,b):
    '''Fuction to find the 
    combination of given numbers [nCr]'''
    c = a-b
    a = factorial(a) #n!
    b = factorial(b) #r!
    c = factorial(c) #(n-r)!
    d = b*c 
    ans = a//d #nCr
    return ans


unipeople = int(input("Enter the number of people in your university: "))
friends = int(input("Enter the number of people you know: "))
meet = int(input("Enter the number of people you are going to meet: "))

P1 = unipeople - friends 
comb1 = combination(P1,meet) #prob. of meeting no friends
comb2 = combination(unipeople,meet) #Sample set
val = comb1/comb2 #Probability = prob. of meeting no friends / Sample set
val = 1 - val # Prob. of meeting atleast one friend = 1 - prob. of meeting no friends
val = round(val,4)
val = val*100 #converting to percentage
print("The chance of you meeting someone you know is {} % ".format(val))
