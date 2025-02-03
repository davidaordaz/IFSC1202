km = float(input("Enter Length of Race in Kilometers: "))
min = float(input("Enter Minutes: "))
sec = float(input("Enter Seconds: "))
miles = km/1.61
hours = (sec/60 + min)/60

print(miles/hours)