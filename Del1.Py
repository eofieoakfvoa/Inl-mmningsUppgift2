import math

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

def GetAreaOfCirclesektor(radien : float, vinkel : float, arc : float):
    arc = arc or None
    vinkel = vinkel or None
    if arc == None:
        if vinkel == None:
            print("please provide a angle")
            return
        arc = (vinkel / 360) * 2*math.pi*radien
    return (arc*radien) / 2
def GetArc(vinkel, )


#print(GetAreaOfTriangle(2, 5))
#print(GetAreaOfParallellogram(2,5))
#print(GetAreaOfCircleRadius(5))
#print(GetAreaOfCircleDiameter(5)) #det tog mig tyvärr lite längre tid än vad det borde för att märka att samma diameter och radien inte ska ge samma svar 
print(GetAreaOfCirclesektor(5, 150))