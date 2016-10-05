# CSC 243-601/610
# Assignment 9
# Fiona Baenziger

# I worked alone

# Correct solutions to these problems will use a loop although
# the majority of work will be done using recursion

import os

# Question 1
def search(fname, path):
    'returns the pathname of a file if it exists or None if it does not'
    for i in os.listdir(path):
        if i[0] != '.':
            if fname == i:
                if '/' in path:
                    return i
                else:
                    return path + '\\' + i
            else:
                file = os.path.join(path, i)
                try:
                    if os.path.isdir(file):
                        call1 = search(fname, file)
                        if "/" in path:
                            return i + '\\' + call1
                        else:
                            return path + '\\' + i + '\\' + call1
                except:
                    pass
                    
# Question 2
def countEndDirs(path):
    'returns the num of directories inside path with no subdirectories'
    try:
        if os.listdir(path) == []:
            return 1
        else:
            for i in os.listdir(path):
                if i[0] != '.':
                    file = os.path.join(path, i)
                    fCount = countEndDirs(file)
                    if os.path.isdir(file):
                        if os.listdir(file) == []:
                            return fCount + 1
                        else:
                            countEndDirs(file)
                            return 0
    except:
        pass
