# CSC 243-601/610
# Assignment 1 
# Fiona Baenziger

# Remember that you are not allowed to use online resources
# when completing assignments

# I worked alone

# Question 1
def computePay():
    'function that computes the pay for an employee with user input'
    hours = eval(input("Enter the hours worked: "))
    payRate = eval(input("Enter the pay rate per hour: "))
    return hours*payRate

# Question 2
def createStr(s, c):
    'function that returns number of times a letter is in  the string'
    numOcc = s.count(c)
    return c*numOcc

# Question 3
def returnN(s, n):
    'function that returns a slice of a string based on user input'
    return s[:n]

# Question 4
def sequences():
    'function that uses range function and for loops to print sequences'
    for i in range(10, 32, 2):
        print(i, end=" ")
    print()
    
    for j in range(14, 77, 7):
        print(j, end=" ")
    print()
    
    for k in range(50, 0, -10):
        print(k, end=" ")

# Question 5
def printChar(lst, index):
    'function that returns a value for the given index for each string in the list'
    for i in lst:
        print(i[index])

