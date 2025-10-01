# Ukazuje rôzne spôsoby iterovania cez dictionary.
# 03_iterating_dict.py

person = {
    "name": "Miso",
    "age": 29,
    "hobby": "music"
}

print("Keys:")
for key in person:
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
