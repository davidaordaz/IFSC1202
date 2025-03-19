x = int(input("Enter the range of numbers:"))
a = []

for i in range(x):
    new_element = int(input())
    a.append(new_element)
    
for j in range(a):
    if(a[i]%2 == 1):
        print(a[i])
        
