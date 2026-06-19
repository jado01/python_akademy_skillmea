import os, random, string

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def ask_yes_no(question):
    while True:
        choice = input(question).strip().lower()
        if choice in ("y", "n"):
            return choice
        else:
            print("Invalid input! Please try again.")

def get_password_options():
    while True:
        try:
            pwd_length = int(input("Enter password length: "))
            if pwd_length < 6:
                print("Password length must be at least 6 characters! Please try again.")
            elif pwd_length > 32:
                print("Maximum length must be 32 characters! Please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid password length!")

    while True:
        lowercase = ask_yes_no("Lowercase letters? (y/n): ")
        uppercase = ask_yes_no("Uppercase letters? (y/n): ")
        numbers = ask_yes_no("Numbers? (y/n): ")
        special_characters = ask_yes_no("Special characters? : (y/n): ")

        options = {"pwd_length": pwd_length, "lowercase": lowercase, "uppercase": uppercase, "numbers": numbers, "specials": special_characters}
        
        if lowercase == "n" and uppercase == "n" and numbers == "n" and special_characters == "n":
            print("All options can't be 'n'! Please try again")
        else:
            return options

def generate_password(data):
    characters = ""
    password_chars = []

    if data["lowercase"] == "y":
        characters += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))
    if data["uppercase"] == "y":
        characters += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))
    if data["numbers"] == "y":
        characters += string.digits
        password_chars.append(random.choice(string.digits))
    if data["specials"] == "y":
        characters += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    remaining_length = data["pwd_length"] - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(random.choice(characters))
    
    random.shuffle(password_chars)
    password = "".join(password_chars)
  
    return password

def main():
    clear_terminal()
    print("""
-=-=-=-=-=-=-=-=-=-
Password Generator
-=-=-=-=-=-=-=-=-=-
1. Generate new password
2. Exit
""")
    
    while True:
        choice = input("Please enter a choice: ").strip()
        if choice == "1":
            options = get_password_options()
            pwd = generate_password(options)
            print(f"Your password is: {pwd}")

        elif choice == "2":
            break
        else:
            print("Invalid input. Please choose 1 or 2")
        
if __name__ == "__main__":
    main()
