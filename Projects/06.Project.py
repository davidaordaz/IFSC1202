outputFile = open("TextFiles/06.Project Output File.txt", "w")
inputFile = open("TextFiles/06.Project Input File.txt", "r")
mergeFile = open("TextFiles/06.Project Merge File.txt", "r")

recordCountInput = 0
recordCountMerge = 0
recordCountOutput = 0



for line in inputFile:
    if line.strip() == "**Insert Merge File Here**":
        for mergeLine in mergeFile:
            outputFile.write(mergeLine)
            recordCountMerge += 1
            recordCountOutput += 1
    else:
        outputFile.write(line)
        recordCountInput += 1
        recordCountOutput += 1

mergeFile.close()
inputFile.close()
outputFile.close()

print(f"{recordCountInput} input file records")
print(f"{recordCountMerge} merge file records")
print(f"{recordCountOutput} output file records")