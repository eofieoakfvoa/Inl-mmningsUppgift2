import os
def CreateTextFile(path, name):
    if not DirectoryExists(path):
        print("Finns ingen map i denna path : ", path)
        return False
    pathAddedWithName = path + "/" + name + ".txt"
    print(pathAddedWithName)
    open(pathAddedWithName, "x")
def WriteToTextFile(path, string):
    file = open(path, "a")

    file.close()

def OverwriteTextFile(path, string):
    pass
def ReadFromTextFile(path):
    file = open(path, "r")
    return file.read()

def DirectoryExists(path):
    return os.path.isdir(path)