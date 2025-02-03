num1 = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
num2 = float(input("Enter Second Number: "))

if(operator == '+'):
    num3 = num1 + num2
    print(num1,'+',num2,'=',num3)
elif(operator == '-'):
    num3 = num1 - num2
    print(num1,'-',num2,'=',num3)
elif(operator == '*'):
    num3 = num1 * num2
    print(num1,'*',num2,'=',num3)
elif(operator == '/'):
    num3 = num1 / num2
    print(num1,'/',num2,'=',num3)
else:
    print("Invalid Operator") 