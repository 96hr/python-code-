import random
def triple_shuffle(l1,l2,l3):
    random.shuffle(l1)
    random.shuffle(l2)
    random.shuffle(l3)
    
    return l1,l2,l3
    
l1=['A', 'B', 'C', 'D']
l2=['OM', 'HARSH', 'UDIT']
l3=[1, 2, 3, 4, 5]
print("BEFORE SHUFFLE:- ")
print(l1)
print(l2)
print(l3)
triple_shuffle(l1,l2,l3)
print("AFTER SHUFFLE:- ")
print(l1)
print(l2)
print(l3)
