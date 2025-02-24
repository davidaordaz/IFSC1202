import math
radiusFile = open("TextFiles/06.01 Radius.txt.")

def diameter(radius):
    return radius * 2

def circumference(radius):
    return diameter(radius) * math.pi

def area(radius):
    return math.pi * pow(radius, 2) 

print(f'{"Radius":>15}', f'{"Diameter":>15}', f'{"Circumference":>15}', f'{"Area":>15}')
for i in radiusFile:
    temp = float(i)
    print(f'{temp:15.5f}', f'{diameter(temp):15.5f}', f'{circumference(temp):15.5f}', f'{area(temp):15.5f}')

radiusFile.close()
    


