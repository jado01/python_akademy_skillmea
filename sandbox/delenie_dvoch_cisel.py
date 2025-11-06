import sys

while True:
    while True:
        try:
            first_number = int(input("Enter a first number please: "))
            break
        except ValueError:
            print("You didn't give a number!")

    while True:
        try:
            second_number = int(input("Enter a second number please: "))
            if second_number == 0:
                print("You can't divide by zero.")
                continue
            else:
                break
        except ValueError:
            print("You didn't give a number!")
            
    result = first_number / second_number
    print(f"The result is: {result}")
    
    while True:
        choice = input("Do You wanna continue?  y/n: ").strip().lower()
        if choice in {"yes", "y", "ano", "áno"}:
            break
        if choice in {"no", "n", "nie"}:
            print("Thank you, the program is over.")
            sys.exit(0)            
        else:
            print("I don't understand, please enter y/n: ")
