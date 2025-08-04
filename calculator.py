# calculatior Program


def calculator():
    k = 1
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    while k == 1:

        print("CALCULATOR")
        print("MENU")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("ADDITION")
            print("Result:", a + b)
        elif ch == 2:
            print("SUBTRACTION")
            print("Result:", a - b)
        elif ch == 3:
            print("MULTIPLICATION")
            print("Reslt:", a * b)
        elif ch == 4:
            if b == 0:
                print("Invalid number for divide")
            else:
                print("DIVISION")
                print("Result:", a / b)
        elif ch==5:
            print("Exit")
            break
        else:
            print("Invalid choice")

        k = int(input("Do you want to continue? (1-Yes / 0-No): "))

calculator()
