try:
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Number: "))

    print("What kind of operation do you want to perform?/nPress + to perform addition/nPress - to perform subtraction/nPress * to perform multiplication/n Press / to perform division")

    operation = input("Enter the operation you want to perform")
    match operation:
        case "+":
            print(f"The sum of {a} and {b} is : {a+b}")

        case "-":
            print(f"The difference of {a} and {b} is {a-b}")

        case "*":
            print(f"The product of {a} and {b} is {a*b}")

        case "/":
            print(f"The reminder of {a} and {b} is {a/b}")
    
        case default:
            print(f"There was an error. Please enter a valid operation.")

except Exception as e:
    print("Please Enter Number Only")
