def CreateTextFile(path, name):
    pass
def WriteToTextFile(path, string):
    file = open(path, "a")

    file.close()

def OverwriteTextFile(path, string):
    pass
def ReadFromTextFile(path):
    file = open(path, "r")
    return file.read()
