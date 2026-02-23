## Python Calculator
print("-----------------------")
print("Calculator :-")
# while loop to run calculator until user quits
while True:
    print("-----------------------")
    print("1.Addition") 
    print("2.Subtraction") 
    print("3.Multiplication") 
    print("4.Division") 
    print("5.Quit") 
    print("-----------------------")

    choice = int(input("Enter Your Choice : "))
    if(choice==5):
        print("Thank U :)")
        break
    n1 = int(input("Enter first number  : "))
    n2 = int(input("Enter second number : "))

    match(choice):
        case(1):
            result = n1+n2
        case(2):
            result = n1-n2
        case(3):
            result = n1*n2
        case(4):
            # To avoid 'division by zero' error used 'continue' so operation do not perform
            if(n2==0):
                print("Result = Division by Zero!!!")
                continue
            result = n1/n2     
        case _:
            print("Invalid Choice!")
            
    print(f"\nResult = {result}")