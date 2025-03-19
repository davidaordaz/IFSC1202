with open("TextFiles/constitution.txt", "r") as file:
    constitutionList = [line.strip() for line in file]

while True:
    searchTerm = input("\nEnter search term: ").strip()

    if searchTerm == "":
        break  

    i = 0
    while i < len(constitutionList):
        if searchTerm in constitutionList[i]:
            startIndex = i
            while startIndex > 0 and constitutionList[startIndex - 1] != "":
                startIndex -= 1

            endIndex = i
            while endIndex < len(constitutionList) - 1 and constitutionList[endIndex + 1] != "":
                endIndex += 1

            print()
            for lineNum in range(startIndex, endIndex + 1):
                print(f"Line {lineNum + 1}: {constitutionList[lineNum]}")
            print()  

            i = endIndex + 1
        else:
            i += 1
