import random

def teams(names):
    if len(names) % 2 != 0:
        raise ValueError("The number of names must be even.")
    random.shuffle(names)
    teams = []
    for i in range(0, len(names), 2):
        teams.append((names[i], names[i+1]))
    return teams
    
names = ["OM", "HARSH", "UDIT", "SANJEEV", "SHIWADITYA", "ANUBHAV"]
result = teams(names)
for i, team in enumerate(result, 1):
    print(f"Team {i}: {team[0]} and {team[1]}")
