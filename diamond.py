import re

# Je vérifie que la saisie rentré est une lettre , donc A à Z , si c'est plusieurs je refuse
# Une fois la saisie correct
# On execute le programme


letter = input("Entre une lettre: ")
regex = "^[A-Z]$"
checkRegex = re.search(regex , letter)

while not checkRegex:
    print("Incorrect entrez une seule lettre en majuscule")
    letter = input("Entre une lettre: ")
    checkRegex = re.search(regex, letter)

n = ord(letter) - 64

for i in range(n * 2 - 1):
    if i >= n:
        i = n * 2 - i - 2
    for j in range(n * 2 - 1):
        print(chr(i + 65) if abs(j - n + 1) == i else " ", end="")
    print()