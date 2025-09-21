age = 19
is_adult = True if age > 18 else False
print("Is adult:", is_adult)

adult_counter = 0
adult_counter += 1 if age > 18 else 0
print("Adult counter:", adult_counter)

adult_name = []
name = "Michal"
adult_name.append(name) if age > 18 else None
print("Adult name list:", adult_name)