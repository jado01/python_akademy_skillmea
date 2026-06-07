# Úloha 10 - Špirála čísel (len pre šikovných)
# Zadaj n a vytvor špirálu čísel n x n.

# Sem napíš svoje riešenie:

while number <= n * n:
    grid[row][column] = number
    number += 1

    next_row = row + direction[aktual_direction][0]
    next_column = column + direction[aktual_direction][1]
    
    if (next_row < 0 or next_row >= n or next_column < 0 or next_column >= n or grid[next_row][next_column] != 0):
        aktual_direction = (aktual_direction + 1) % 4

        row = row + direction[aktual_direction][0]
        column = column + direction[aktual_direction][1]

    else:
        row = next_row
        column = next_column

for r in grid:
    print(r)