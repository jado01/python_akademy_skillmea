#Ukazuje vytvorenie dictionary, prístup k hodnotám a zmenu.
# 01_basic_dict.py

person = {
    "name": "Janko",
    "age": 30,
    "country": "Slovensko"
}

print(person)

# Access value by key
print(person["name"])

# Change a value
person["age"] = 31
print(person)

# Add a new key-value pair
person["hobby"] = "cycling"
print(person)
