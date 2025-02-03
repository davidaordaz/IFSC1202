numSeconds = float(input("Enter Number of Seconds: "))

numYears = numSeconds / (60*60*24*365)
numSeconds %= (60*60*24*365)

numDays = numSeconds / (60*60*24)
numSeconds %= (60*60*24)

numHours = numSeconds / (60*60)
numSeconds %= (60*60)

numMinutes = numSeconds / 60
numSeconds %= 60

print("Years:",int(numYears))
print("Days:",int(numDays))
print("Hours:",int(numHours))
print("Minutes:",int(numMinutes))
print("Seconds:",int(numSeconds))

