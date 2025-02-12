num1 = int(input("Enter Start of Range: "))
num2 = int(input("Enter End of Range: "))
print("Special Numbers Between", num1, "and", num2)


for i in range(num1, num2):
    temp1 = i
    temp2 = i
    count = 0
    num3 = 0
    while temp1 >= 1:
        temp1 //= 10
        count += 1
    for j in range(0, count):
        num3 += pow(temp2%10, count)
        temp2 = int(temp2/10)
    if(num3 == i):
        print(num3)