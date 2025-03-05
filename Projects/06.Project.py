outputFile = open("TextFiles/06.Project Output File.txt", "w")
inputFile = open("TextFiles/06.Project Input File.txt", "r")
mergeFile = open("TextFiles/06.Project Merge File.txt", "r")
recordCountInput = 0
recordCountMerge = 0



line = inputFile.readline()
while line != '':
    if(line == "**Insert Merge File Here**\n"):
        for i in mergeFile:
        line = mergeFile.readline()
        print(line)
        recordCountMerge += 1
    else:
        print(line)
        recordCountInput += 1
    line = inputFile.readline()

mergeFile.close()
inputFile.close()
outputFile.close()

