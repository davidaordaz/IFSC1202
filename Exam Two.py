a = []

with open("TextFiles/Exam Two Names.txt") as nameFile:
    for line in nameFile:
        y = line.strip().split(", ")  # Remove newlines and split into pairs
        a.append(y)




x = input("Enter a Name: ").strip().capitalize()

while x.lower() != "q":
    isFound = False

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == x:
                if j == 0:
                    print("Boy's Name - Rank:", i + 1)
                else:
                    print("Girl's Name - Rank:", i + 1)
                isFound = True
                break
        if isFound:
            break

    if not isFound:
        print("Name Not Found")
        
    x = input("Enter a Name: ").strip().capitalize()
    
                
                

