# CSC 243-601/610
# Assignment 8
# Fiona Baenziger

# I worked alone

import os

def strFold(s1, s2):
    'a recursive function that take two strings and returns a combination of the two'
    if len(s1) == 0 and len(s2) == 0:
        return ''
    elif len(s1) == 0:
        word = strFold(s1, s2[1:])
        return s2[0] + word
    elif len(s2) == 0:
        word = strFold(s1[1:], s2)
        return s1[0] + word
    else:
        word = strFold(s1[1:], s2[1:])
        add = s1[0] + s2[0]
        return add + word

def strCount(lst):
    'a recursive function that takes nested lists and returns number of str in list'
    if len(lst) == 0:
        return 0
    elif type(lst[0]) != list:
        if type(lst[0]) == str:
            quest = strCount(lst[1:])
            return quest + 1
        else:
            quest = strCount(lst[1:])
            return quest
    else:
        quest1 = strCount(lst[0])
        quest2 = strCount(lst[1:])
        return quest1 + quest2
        

def findMax(lst):
    'a recursive function that takes a nested list and returns the maximum value'
    if len(lst) == 0:
        return 0
    elif type(lst[0]) != list:
        num = findMax(lst[1:])
        if num > lst[0]:
            return num
        else:
            return lst[0]
    else:
        num1 = findMax(lst[0])
        num2 = findMax(lst[1:])
        if num1 > num2:
            return num1
        else:
            return num2

def printDirs(path, indent):
    'a recursive function that takes path and prints the name of every subfolder'
    try:
        for i in os.listdir(path):
            if i[0] != '.':
                file = os.path.join(path, i)
                if os.path.isdir(file):
                    print((indent * '   ') + file)
                    printDirs(file, indent+1)
    except:
        print("'{}' is not a file or directory.".format(path))
