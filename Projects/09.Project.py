import csv

fileName = "09.Project Distances.csv"

with open(fileName, newline='') as file:
    reader = csv.reader(file)
    table = []
    for row in reader:
        table.append(row)

for row in table:
    for item in row:
        print(item, end="\t")
    print()

fromCity = input("Enter From City: ")
toCity = input("Enter To City: ")

rowIndex = -1
for i in range(len(table)):
    if table[i][0].lower() == fromCity.lower():
        rowIndex = i
        break

colIndex = -1
for j in range(len(table[0])):
    if table[0][j].lower() == toCity.lower():
        colIndex = j
        break

if rowIndex == -1:
    print("Invalid From City")
elif colIndex == -1:
    print("Invalid To City")
else:
    distance = table[rowIndex][colIndex]
    print(fromCity + " to " + toCity + " - " + distance + " miles")
