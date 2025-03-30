import os
def CreateTextFile(path, name):
    pathAddedWithName = path + "/" + name + ".txt"
    if not DirectoryExists(path):
        print("Finns ingen map i denna path : ", path)
        return False
    if FileExists(pathAddedWithName):
        print("Det finns redan en fil med det namnet i vald mapp : ", pathAddedWithName)
        return False
    open(pathAddedWithName, "x")
    return True, pathAddedWithName
def WriteToTextFile(path, string):
    file = open(path, "a")
    file.close()

def OverwriteTextFile(path, string):
    pass
def ReadFromTextFile(path):
    file = open(path, "r")
    return file.read()

#dessa är mäst till för att det ser finare ut där de används
def DirectoryExists(path):
    return os.path.isdir(path)
def FileExists(path):
    return os.path.exists(path)