import random

my_list = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Joseph", "Yves", "Preeti", "Nadiya", "Aida", "Augustin", "Klebert", "Marc", "Sofia", "Younes", "Kenny", "Floriane", "Jordi", "Alberto", "Fang", "Caterina", "Yassine", "Dragos", "Hanieh", "Mengstu", "test1", "test2", "test3", "test", "test5"]
random.shuffle(my_list)
people = random.sample(my_list, 24)
print(people)
remaining_persons = list[set(my_list) - set(people)]

tables = [[],[],[],[],[],[]] # Number of tables defined for test

def define_table(people):
    i = 0
    while len(people)>= 4:
        tables[i].append(people[0:4])
        del people[0:4]
        i += 1
    
    for idx, table in enumerate(tables, start=1):
        print(f"Table {idx}: {table}")


def last_ones(people):
    if len(people) == 3:
        tables[i].append(people[0:3]) 

    elif len(people) == 2:
        tables[i].append(people[0:2])
    
    elif len(people) == 1:
        tables[1].append(people[0]) 

    return tables #print les listes créées
  
define_table(people)
last_ones(people)

if len(my_list) >= 24:
        print(f"Sorry {remaining_persons}, the first room is full. You should rent another one.")