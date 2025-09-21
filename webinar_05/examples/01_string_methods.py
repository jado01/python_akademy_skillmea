# Použi rôzne stringové metódy na vlastný text.

name = "michal hucko"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

text = "Hello world"
print(text.replace("world", "Python"))

text_with_spaces = "   Hello world   "
print(text_with_spaces.strip())
print(text_with_spaces.lstrip())
print(text_with_spaces.rstrip())