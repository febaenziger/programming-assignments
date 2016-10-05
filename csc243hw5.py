# CSC 243-601/610
# Assignment 5
# Fiona Baenziger

# I worked alone

# You can change this import statement if you like
from random import randint

# Question 1
def table(fname, n):
    'returns a two-dimensional list containing a list of variant n*n numbers'
    try:
        file = open(fname, "r")
        fileC = file.read()
        file.close()
           
        lstOut = []
        index = 0
        for j in range(n):
            partLst = []
            for k in range(n):
                try: #if n is out of range
                    partLst.append(int(fileC.split()[index]))
                    index += 1
                except:
                    pass
            lstOut.append(partLst)               
        return lstOut
       
    except:
        return []

# Question 2
def makeNoisy(table, numChanges):
    'takes table and randomly changes numChanges numbers in random rows'
    try:
        for i in range(numChanges):
            ranRow = randint(0, (len(table)-1))
            ranInd = randint(0, (len(table[ranRow])-1))
            ranNum = randint(0, 255)
            table[ranRow][ranInd] = ranNum
    except:
        pass
            
# Question 3
def lookup_name(file):
    'takes user input, reads the file, and prints corresponding name'
    try:
        fname = open(file, "r")
        fContent = fname.readlines()
        fname.close()

        nameDict = {}
        for i in fContent:
            i = i.split()
            nameDict[i[1]] = i[0]
            
        cond = True
        while cond == True:
            nickname = input("Enter a nickname: ")
            if nickname == "":
                cond = False
            elif nickname in nameDict:
                print("The corresponding name is {}.".format(nameDict[nickname]))
            else:
                print("Not Found.")
                    
    except IOError:
        return "{} could not be opened. Exiting...".format(file)

