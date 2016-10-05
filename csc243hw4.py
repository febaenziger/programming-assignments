# CSC 243-601/610
# Assignment 4
# Fiona Baenziger

# Remember that you are not allowed to use online resources
# when completing assignments

# I worked alone

# Include doc strings for full credit

# Question 1
def statement(accountlst):
    'takes list of floats and returns list with one sum of positive and one sum negative'
    negative = 0
    positive = 0
    
    for i in accountlst:
        if i >= 0:
            positive += i
        else:
            negative += i
    return [positive, negative]

# Question 2
def pairSum(lst, n):
    'prints the indices of values in lst that sum up to n'
    sumNum = 0
    noRe = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j not in noRe and (i != j):
                noRe.append(i)
            if ((lst[i] + lst[j]) == n) and i not in noRe:
                print('{} {}'.format(i, j))
        
# Question 3
def printParity(lst):
    'prints number of rows in lst that are even and number of rows that are odd'
    even = 0
    odd = 0

    for i in range(len(lst)):
        sumNum = 0
        for j in range(len(lst[i])):
            sumNum += lst[i][j]           
        if sumNum % 2 == 0:
            even += 1
        else:
            odd += 1
    print("There are {} even rows and {} odd rows in the list.".format(even, odd))

# Question 4
def findMaxDiff(lst):
    'prints index of row with max difference and value of max difference from row'
    maxNum = 0
    maxIndex = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for k in range(len(lst[i])):
                if abs(lst[i][j]-lst[i][k]) > maxNum:
                    maxNum = abs(lst[i][j]-lst[i][k])
                    maxIndex = i
    if maxNum == 0:
        maxIndex = i
    print("The maximum difference of {} is found in row {}.".format(maxNum, maxIndex))
        
# Question 5
def printMinMax():
    'prints min and max number that user inputs and stops when negative or zero'
    numLst = []
    cond = True

    while cond == True:
        try:
            num = int(input("Please enter a number: "))
            if num > 0:
                numLst.append(num)
            else:
                newLst = []
                for i in numLst:
                    if i not in newLst:
                        newLst.append(i)
                if len(newLst) < 2:
                    print("Fewer than two positive integers were entered.")
                else:
                    print("The minimum value is {} and the maximum value is {}.".format(min(numLst), max(numLst)))
                cond = False
        except:
            print("That was not a valid number. Please try again.")
