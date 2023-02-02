ascii_number = 65
rows=int(input())
for i in range(0, rows):
    for j in range(0, rows):
        character = chr(ascii_number)
        print(character, end=' ')
    ascii_number += 1
    print()