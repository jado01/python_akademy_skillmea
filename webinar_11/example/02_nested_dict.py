# Ukazuje vnorený dictionary a prístup k vnoreným hodnotám.
# 02_nested_dict.py

person = {
    "name": "Eva",
    "adress": {
        "street": "Hlavna",
        "number": 25,
        "postal code": "040 01"
    }
}

print(person)
print(person["adress"]["street"])  # Access nested key
