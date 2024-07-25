num1=float(input("Enter a number:"))
num2=float(input("Enter another number:"))

print("pass1 for addition \n pass2 for subtraction  \npass 3 for multiplication  \n pass4 for division")

choice=int(input("enter the choice from 1-4:"))

if choice==1:
    a=num1+num2
    print(a)
elif choice==2:
    s=num1-num2
    print(s)
elif choice==3:
    m=num1 * num2
    print(m)
elif choice==4:
    d=num1 // num2
    print(d)

