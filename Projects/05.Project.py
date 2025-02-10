num1 = int(input("Enter Start of Range: "))
num2 = int(input("Enter End of Range: "))
print("Special Numbers Between", num1, "and", num2)


for i in range(num1, num2):
    temp = i
    count = 0
    num3 = 0
    while num1 > 0:
        num1 //= 10
        count += 1
    for j in range(count):
        temp%=10
        num3 += temp^count
    if(num3 == temp):
        print(num3)