# CSC 243-601/610
# Assignment 3
# Fiona Baenziger

# Remember that you are not allowed to use online resources
# when completing assignments

# I worked alone

# Question 1
def separateWords(fname):
    'takes string from fname and writes words starting with vowels to vowel.txt & consonants to consonants.txt'
    file = open(fname, 'r')
    fileContents = file.read()
    file.close()

    editFile = ""
    for i in fileContents:
        if i not in ["!", "?", ":", ",", ".", ";"]:
            editFile += i

    vowel = open("vowel.txt", "w")
    consonant = open("consonant.txt", "w")
    
    for j in editFile.split():
        if j[0].lower() in ["a", "e", "i", "o", "u"]:
            vowel.writelines(j + '\n')
        else:
            consonant.writelines(j + '\n')

    vowel.close()
    consonant.close()

# Question 2
def printSubStrs(slst):
    'prints, one per line, if the string in the list are substrings of their predecessor'
    for i in range(1, len(slst)):
        if slst[i].lower() in slst[i-1].lower():
            print(slst[i].lower())

# Question 3
def constantDiff(s, n):
    'returns True if difference in adjacent characters in s equals n and returns False if not.'
    ans = False
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == n:
            ans = True
        else:
            return False
    return ans
            
# Question 4
def shiftN(s, n):
    'takes string parameter s and returns the string shifted down n'
    new = ""
    for i in s:
        shift = ord(i)+n
        while shift >= 123:
            shift -= 26
        new += chr(shift)
    return new

# Question 5
def findIndices(s):
    'returns list of indices in the string where digits can be found'
    intLst = []
    for i in range(len(s)):
        if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            intLst.append(i)
    return intLst
        


