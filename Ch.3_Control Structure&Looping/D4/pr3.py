num1 = int(input("Enter a number for A:"))
num2 = int(input("Enter a number for B:"))
num3 = int(input("Enter a number for C:"))


if num1==num2 and num2==num3:
    print("All are same")
else :
    if num1==num2:
        print("A and B are same")
    elif num2==num3:
        print("B and C are same")
    elif num1==num3:
        print("A and C are same")
    else:
        if num1>num2:
            if num1>num3:
                print("A is largest number")
            else:
                print("C is largest number")
        else:
            if num2>num3:
                print("B is largest number")
            else:
                print("C is largest number")



