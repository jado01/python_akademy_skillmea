def count_to(n):
    i = 1
    while i < n:
        yield i
        i += 1

g = count_to(3)
print(next(g))
print(next(g))
#  print(next(g)) pri tomto dalsiom riadku s enxt dostamen Trackback

def read_numbers(path):
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            yield int(line)

g = read_numbers("data.txt")
print([num for num in g])

for num in read_numbers("data.txt"):
    print(num)

# z listu comprehension viem vytvorit generator vymenou hranatych zatvoriek [] za okruhle zatvorky ()

number = (x for x in range(100000000))
print(number)