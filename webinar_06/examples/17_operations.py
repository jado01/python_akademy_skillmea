ages = [29, 33, 45, 24]

ages[1] = 50
print("Menenie hodnoty:", ages)

ages[1:3] = [0, 0]
print("Nahradenie slicingu:", ages)

ages.append(10)
print("Po append:", ages)

ages.remove(0)
print("Po remove:", ages)

ages.extend([1, 1])
print("Po extend:", ages)

ages.insert(2, "Michal")
print("Po insert:", ages)

print("Počet výskytov 1:", ages.count(1))
print("Index prvého výskytu 1:", ages.index(1))
