import Del2Modul
import os

def Main():
    running = True
    previousUsedFile = None
    while running: #sålänge running är true kommer programmet att repeata
        print("Skriv en av följande eller inget för att gå ut  \n",
              "[Write] för att skriva till en textfil \n",
              "[Overwrite] för att skriva över en textfil \n",
              "[Read] för att läsa från en text fil \n",
              "[Create] för att skapa en text fil\n",
              "[] för att stänga programmet")
        userInput = input().lower()
        if userInput == "write":
            success = WriteToFile(previousUsedFile, "a") # "a" = append, jag tycker att det är lättare för användarn att write är inte att man skriver över allt
            if success != None: #kanske borde gjort såhär när man skapar en fil (jag skrev detta efter jag skrev create metoden)
                previousUsedFile = success
        elif userInput == "overwrite":
            success = WriteToFile(previousUsedFile, "w") # "w" = write, som betyder att den skriver över allt
            if success != None: #kanske borde gjort såhär när man skapar en fil (jag skrev detta efter jag skrev create metoden)
                previousUsedFile = success
        elif userInput == "read":
            ReadFromFile(previousUsedFile)
        elif userInput == "create":
            success = CreateFile() 
            print(success)
            if success != False: #kanske inte är det bästa sättet att göra detta men eftersom ifall den är false så har den bara 1 value och inte 2 som true har, så skulle success[0] == true, gå på grund av false och detta funkar
                previousUsedFile = success[1]
        elif userInput == "":
            print("stänger nu programmet")
            running = False
        else:
            print("kontrollera att du skrev rätt, du skrev ", userInput)
            
def CreateFile():
    print("Skriv först ett namn till filen")
    name = input()
    print("Skriv nu en path till vart du vill att den ska vara eller [Current] för att få den i samma map som denna är i")
    choice = input()
    Success = None
    if choice.lower() == "current": #lower() för att t.ex Current ska fungera eller cURRENT, jag sätter det inte i input() delen eftersom jag vet inte ifall paths är case sensitive, därför gör jag det härh
        Success = Del2Modul.CreateTextFile(os.path.abspath(os.getcwd()), name)
    else:
        Success = Del2Modul.CreateTextFile(choice, name)
    if not Success:
        print("Det gick inte att skapa en fil")
        return False
    elif Success:
        print("Det gick att skapa en fil! :D")
        return Success

def WriteToFile(previousUsedFile, appendorwrite):
    print("Skriv en path till en text fil eller skriv [Current] för att använda senast använd fil i detta program som är : ", previousUsedFile) #previousUsedFile blir "None" ifall den inte har en value än
    choice = input()
    print("Skriv nu vad som ska skrivas i filen")
    text = input()
    if choice.lower() == "current":
        choice = previousUsedFile
    Success = Del2Modul.WriteToTextFile(choice, text, appendorwrite)
    if Success == True:
        return choice
    return None
def ReadFromFile(previousUsedFile):
    print("Skriv en fil path att läsa från eller skriv [Current] för att använda senast använd fil i detta program som är : ", previousUsedFile)
    choice = input()
    if choice.lower() == "current":
        choice = previousUsedFile
    Success = Del2Modul.ReadFromTextFile(choice)
    if Success != False:
        print("Läser från filen\n",Success, "\n ")
Main()