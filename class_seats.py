import random

people = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Yves", "Preeti", "Nadiya", "Aida", "Augustin", "Klebert", "Marc", "Sofia", "Younes", "Kenny", "Floriane", "Jordi", "Alberto", "Fang", "Caterina", "Yassine", "Dragos", "Hanieh", "Mengstu"]
random.shuffle(people)
#print(people)


tables = [[],[],[],[],[],[]] # Number of tables defined for test

def define_table(people):
    i = 0
    while len(people)> 0:
        tables[i].append(people[0:4])
        del people[0:4]
        i += 1

    for idx, table in enumerate(tables, start=1):
            print(f"Table {idx}: {table}")

       

       

    return tables #print les listes créées
        
print(define_table(people))
