# CSC 243-601/610
# Assignment 2
# Fiona Baenziger

# Remember that you are not allowed to use online resources
# when completing assignments

# I worked alone

# Include doc strings for full credit

# Question 1
def customSpam(name, amount, address):
    'prints customized spam using the parameters name, amount, and address'
    newName = ""
    for i in (name.title()).split():
        newName += " " + i
        
    print("Dear " + newName.strip() + ", \nWe would like to let you know about a great oppurtunity. \nYou can make "
          + " ".join(amount.upper()) + " dollars in just a few short weeks! \nThis is a limited-time offer. \nPlease contact us at "
          + address + " for more information.")

# Question 2
def countName(nlst, name):
    'return the number of times name appears in nlst'
    count = 0
    for i in nlst:
        if i.lower() == name.lower():
            count += 1
    return count

# Question 3
def numTimes(s, word):
    'returns the number of times the string word appears in sentence s'
    editS = ""
    for i in s:
        if i not in ["!", "?", ":", ",", ".", ";"]:
            editS = editS + i
    count = 0
    for j in editS.split():
        if j.lower() == word.lower():
            count += 1
    return count

# Question 4
def countLen(fname, n):
    'returns number of words in fname that have n characters'
    file = open(fname, 'r')
    fileContents = file.read()
    file.close()

    editFile = ""
    for i in fileContents:
        if i not in ["!", "?", ":", ",", ".", ";"]: 
            editFile = editFile + i
    count = 0
    for j in editFile.split():
        if len(j) == n:
            count += 1
    return count
    
# Question 5
def printLarger(fname, val):
    'reads numbers in fname and prints ones larger or greater than n'
    numFile = open(fname, 'r')
    numFileCont = numFile.read()
    numFile.close()

    for i in numFileCont.split():
        if eval(i) > val:
            print(i)

