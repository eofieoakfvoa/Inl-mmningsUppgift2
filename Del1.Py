import math #används för att få t.ex math.pi

#jag använder mig av : float för det gör det lättare att se vad den förväntar sig när man använder sig av den,
#t.ex så stor det istället för base = any så står det base = float, så då vet man ungefär vad den förväntar sig.
#Jag har ingen error handling eftersom jag tror det är bättre ifall man förväntar sig att där den används har error handling istället
#ett problem kan vara problem med floating point error, jag vet inte hur man fixar det och jag vet inte hur fel svaren är pågrund av det, 
#det skulle gå att avrunda svaret så borde det vara mer accurate
def GetAreaOfTriangle(base : float, height : float):
    return (base * height) / 2

def GetAreaOfParallellogram(base : float, height : float):
    return base * height

def GetAreaOfParallelltrapets(baselength : float, toplength : float, height : float):
    return (height * (baselength + toplength)) / 2

def GetAreaOfCircleRadius(radien : float):
    return math.pi * radien**2

def GetAreaOfCircleDiameter(diameter : float):
    return (math.pi * diameter**2) / 4

def GetAreaOfCirclesektor(radien : float, vinkel : float, arc = None):
    if arc == None:
        if vinkel == None:
            print("please provide an angle or an arc")
            return
        arc = GetArc(vinkel, radien)
    return (arc*radien) / 2
def GetArc(vinkel : float, radien : float):
    return (vinkel / 360) * 2*math.pi*radien

print(GetAreaOfTriangle(2, 5))
print(GetAreaOfParallellogram(2,5))
print(GetAreaOfCircleRadius(5))
print(GetAreaOfCircleDiameter(5)) #det tog mig tyvärr lite längre tid än vad det borde för att märka att samma diameter och radien inte ska ge samma svar 
print(GetAreaOfCirclesektor(5, 120, GetArc(120, 5)))
print(GetAreaOfCirclesektor(5, 120))