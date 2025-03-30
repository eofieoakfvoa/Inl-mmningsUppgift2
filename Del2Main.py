import Del2Modul
import os

def Main():
    running = True
    previousUsedFile = None
    while running:
        print(previousUsedFile)
        print("Skriv en av följande eller inget för att gå ut  \n",
              "[Write] för att skriva till en textfil \n",
              "[Overwrite] för att skriva över en textfil \n",
              "[Read] för att läsa från en text fil \n",
              "[] för att stänga programmet")
        userInput = input().lower()
        if userInput == "write":
            pass
        elif userInput == "overwrite":
            pass
        elif userInput == "read":
            pass
        elif userInput == "create":
            success = CreateFile()
            if success[0] == True:
                previousUsedFile = success[1]
        elif userInput == "":
            running = False
        else:
            print("kontrollera att du skrev rätt, du skrev ", userInput)
def CreateFile():
    print("Skriv först ett namn till filen")
    name = input()
    print("Skriv nu en path till vart du vill att den ska vara eller [Current] för att få den i samma map som denna är i")
    choice = input()
    Success = None
    if choice.lower() == "current":
        Success = Del2Modul.CreateTextFile(os.path.abspath(os.getcwd()), name)

    if not Success:
        print("Det gick inte att skapa en fil")
    elif Success:
        print("Det gick att skapa en fil! :D")
        return Success



Main()