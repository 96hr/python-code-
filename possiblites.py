import itertools
options = {
    'color': ['red', 'blue', 'green'],
    'size': ['small', 'medium', 'large'],
    'material': ['cotton', 'wool', 'silk']
}
possibilities = list(itertools.product(*options.values()))

for combo in possibilities:
    print(combo)
