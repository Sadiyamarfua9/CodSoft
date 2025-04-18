opr1=int(input("Enter the first operand: "))
opr2=int(input("Enter the second operand: "))
def Calci(opr1,opr2):
    print("----------CALCULATOR----------")
    print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
    choice=input("Enter your choice from 1 to 4:\n")
    if choice == '1': 
        print(f"Sum of {opr1} + {opr2} = {opr1+opr2}")
    elif choice == '2': 
        print(f"Difference of {opr1} - {opr2} = {opr1-opr2}")
    elif choice == '3': 
        print(f"Product of {opr1} * {opr2} = {opr1*opr2}")
    elif choice == '4': 
        if opr2 != 0:
            print(f"Quotient of {opr1} / {opr2} = {opr1/opr2}")
        else:
            print("Dividing a number by zero is not possible") 
    else:
        print("Enter a valid choice")
Calci(opr1,opr2)

    

