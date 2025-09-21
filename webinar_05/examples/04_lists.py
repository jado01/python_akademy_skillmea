grade_list = [1, 1, 2, 3, "Michal", "Janko", 2.5, True]
print(grade_list)
print(grade_list[0])      # 1
print(grade_list[0:2])    # [1, 1]
print(grade_list[-4:])    # ['Michal', 'Janko', 2.5, True]

nested = [1, 2, "Ferko"]
grade_list.append(nested)

print(grade_list[-1])       # [1, 2, "Ferko"]
print(grade_list[-1][-1])   # Ferko
print(grade_list[-1][-1][-1])  # o