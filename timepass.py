def print_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)
rows = 5
print_diamond(rows)

def print_cartoon_face():
    print("  _____   ")
    print(" /     \\ ")
    print("|  O O  |")
    print("|   ^   |")
    print(" \\ --- / ")
    print("  -----  ")

print_cartoon_face()
