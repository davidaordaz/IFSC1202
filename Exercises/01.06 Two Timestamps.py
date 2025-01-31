print("First Timestamp")

hours = int(input("Enter Hours: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))
totalTime1 = hours*60**2 + min*60 + sec

print("Second Timestamp")
hours = int(input("Enter Hours: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))
totalTime2 = hours*60*60 + min*60 + sec

difference = abs(round(totalTime1 - totalTime2))
print("Difference of Timestamps: ",difference,"seconds.")