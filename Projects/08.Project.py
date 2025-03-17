#might need to start over next time 
# the searchIndex is way off so code is not detecting the correct index of liquor


constitutionFile = open("TextFiles/constitution.txt", "r")
constitutionList = []
searchTerm = str(input("Enter Search Term: "))
searchIndex = 0
startIndex = 0
endIndex = 0

for line in constitutionFile:
    constitutionList.append(line)

for i in range(len(constitutionList)):
    if(searchTerm in constitutionList[i]):
        searchIndex = i
        break

for j in reversed(range((constitutionList[searchIndex]))):
    if("" in constitutionList[searchIndex - j]):
        startIndex = j
        break

for h in range((constitutionList[startIndex])):
    if("" in constitutionList[searchIndex - startIndex + 1]):
        endIndex = h
        break

for k in range((constitutionList[startIndex])):
    if(constitutionList[k] == ""):
        print("Line", startIndex + k + 1,":", constitutionList[startIndex + k])
        break
    else:
        print("Line", startIndex + k + 1,":", constitutionList[startIndex + k])




constitutionFile.close()