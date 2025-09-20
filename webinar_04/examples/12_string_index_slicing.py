# Skús indexovanie a slicing na rôznych reťazcoch.



meno = input("Zadaj meno:\n")
print(f"Pracujeme aktualne s retazcom: {meno}")
print("Dlzka retazca:", len(meno))
print("Druhy znak je:", meno[1])
print("Prve dva znaky su:", meno[:2])
print("Osekane od -3 do -1:", meno[-3: -1])
print("Osekane od -2 po koniec:", meno[-2:])
