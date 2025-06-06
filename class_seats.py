import random

people = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Yves", "Preeti", "Nadiya", "Aida", "Augustin", "Klebert", "Marc", "Sofia", "Younes", "Kenny", "Floriane", "Jordi", "Alberto", "Fang", "Caterina", "Yassine", "Dragos", "Hanieh", "Mengstu"]
random.shuffle(people)
print(people)


tables = [[],[],[],[],[],[]] # Number of tables defined for test

def define_table(people):
    i = 0
    while len(people)> 0:
        tables[i].append(people[0])
        people.pop(0)
        if len(tables[i] == 4):
            continue
        i += 1
                
    else:
        if len(people) == 3:
            tables[i].append(people[0,2])
        elif len(people) == 2:
            tables[i].append(people[0,1])
        elif len(people) == 1:
            tables[i].append(people[0])

    return tables #print les listes créées
        
print(define_table(people))
