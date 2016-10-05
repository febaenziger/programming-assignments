import os

def search(fname, path):
    d = os.listdir(path)
    if fname in d:
        return os.path.join(path, fname)
    for item in d:
        itemPath = os.path.join(path, item)
        try:
            p = search(fname, itemPath)
            if p != None:
                return p
        except:
            pass
    return None


def countEndDirs(path):
    hasDir = False
    count = 0
    for item in os.listdir(path):
        itemPath = os.path.join(path, item)
        if os.path.isdir(itemPath):
            hasDir = True
            count += countEndDirs(itemPath)
    if not hasDir:
        count += 1
    return count
