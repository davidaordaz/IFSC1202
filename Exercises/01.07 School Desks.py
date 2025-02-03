classA = int(input("Enter Classroom A: "))
classB = int(input("Enter Classroom B: "))
classC = int(input("Enter Classroom C: "))
x = classA + classB + classC
numDesks = int(x / 2 + x % 2)
print(numDesks)
