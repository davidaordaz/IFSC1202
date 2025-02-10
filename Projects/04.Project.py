x = int(input("Enter Maximum Height: "))

for i in range(x+1):
    for j in range(i):
        print("*", end = " ")
    print("")

for x in range(x-1,0,-1):
    for h in range(x):
        print("*", end = " ")
    print("")


    