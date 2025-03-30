import Del2Modul
import os

def Main():
    running = True
    previousUsedFile = None
    while running:
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
            CreateFile()
        
        elif userInput == "":
            pass
        else:
            print("kontrollera att du skrev rätt, du skrev ", userInput)
def CreateFile():
    print("Skriv först ett namn till filen")
    name = input()
    print("Skriv nu path till vart du vill att den ska vara eller [Current] för att få den i samma map som denna är i")
    choice = input()
    if choice.lower() == "current":
        Del2Modul.CreateTextFile(os.path.abspath(os.getcwd()), name)

Main()