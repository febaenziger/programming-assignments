# CSC 243-601/610
# Assignment 7
# Fiona Baenziger

# I worked alone

# Question 1
def countdown(n):
    'a recursive countdown that prints a silly message between 3 and 2'
    if n <= 0:
        print("Blast off!")
    elif n == 3:
        print("3\nBoom!\nDid I scare you?")
        countdown(n-1)
    else:
        print(n)
        countdown(n-1)

# Question 2
def recHourGlass(c1, c2, n, indent):
    'a recursive function that prints out an hour glass pattern'
    if n <= 0:
        return
    else:
        print((indent*" ") + (c1*n))
        recHourGlass(c1, c2, n-2, indent+1)
        print((indent*" ") + (c2*n))

# Question 3
def printPattern(indent, n):
    'a recursive function that prints a pattern with asterics'
    if n <= 0:
        return
    else:
        printPattern(indent, n//2)
        print((' ' * indent) + ('*' * n))
        printPattern(indent+(n//2), n//2)

# Question 4
def recSum(k, n):
    'recursively returns the sum of the numbers between k and n'
    if k > n:
        return 0
    else:
        sumNum = recSum(k, n-1)
        return n + sumNum

# Question 5
def recSpaceCount(s):
    'recursively returns the number of white spaces in the string parameter'
    if len(s) == 0:
        return 0
    else:
        if s[0].isspace() == True:
            add = recSpaceCount(s[1:])
            return add + 1
        else:
            return recSpaceCount(s[1:])
            
