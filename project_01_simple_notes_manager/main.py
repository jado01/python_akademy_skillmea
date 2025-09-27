menu = "" \
"Simple Notes Manager\n" \
"====================\n" \
"1. List Notes\n" \
"2. Add a Note\n" \
"3. Delete a Note\n" \
"4. Exit\n" \

print(menu)

while True:
    option = int(input("Choose an option (1?4):\n"))
    if option == 3:
        delete_notes = print("Enter the ID of the note to delete:")
    elif option == 4:
        print("Goodbye!")
        break