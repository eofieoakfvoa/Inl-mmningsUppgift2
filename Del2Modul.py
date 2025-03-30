import os

def CreateTextFile(path, name):
    pathAddedWithName = path + "/" + name + ".txt"
    if not DirectoryExists(path):
        print("Finns ingen map i denna path : ", path)
        return False
    if FileExists(pathAddedWithName):
        print("Det finns redan en fil med det namnet i vald mapp : ", pathAddedWithName)
        return False
    open(pathAddedWithName, "x") #x skapar fil, tror den delen av open() liksom bestämmer permissions
    return True, pathAddedWithName

def WriteToTextFile(path, string, writeorappend):
    if not FileExists(path) or DirectoryExists(path): #detta kollar så att det inte är en mapp och att path leder någon stans, jag vet inte ifall man kan kolla ifall det är en .txt fil, man skulle typ kunna göra en for loop som börjar från slutet och kollar att det innehåler t, x, t
        print("Filen existerar inte eller så skrev du en mapp") 
        return False
    file = open(path, writeorappend) #eftersom jag implimenterar writeorappend delen och det inte är usern som gör det så borde det inte riskera att man gör något fel
    file.write(string)
    file.close() # vet inte ifall detta behövs men gör det för det stog så i en av källorna
    return True

def ReadFromTextFile(path):
    if not FileExists(path) or DirectoryExists(path): #detta kollar så att det inte är en mapp och att path leder någon stans, jag vet inte ifall man kan kolla ifall det är en .txt fil, man skulle typ kunna göra en for loop som börjar från slutet och kollar att det innehåler t, x, t
        print("Filen existerar inte eller så skrev du en mapp") 
        return False
    file = open(path, "r") #r står för read
    return file.read()

#dessa är mest till för att det ser finare ut där de används
def DirectoryExists(path):
    return os.path.isdir(path)
def FileExists(path):
    return os.path.exists(path)