import random

<<<<<<< HEAD
people = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Yves", "Preeti",  "Aida", "joseph"]
random.shuffle(people)
#print(people)

=======
my_list = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Joseph", "Yves", "Preeti", "Nadiya", "Aida", "Augustin", "Klebert", "Marc", "Sofia", "Younes", "Kenny", "Floriane", "Jordi", "Alberto", "Fang", "Caterina", "Yassine", "Dragos", "Hanieh", "Mengstu", "test1", "test2", "test3", "test", "test5"]
random.shuffle(my_list)
people = random.sample(my_list, 24)
print(people)
remaining_persons = list[set(my_list) - set(people)]
>>>>>>> 23ea96459fa6afc160c68b8811165e3d2fd8580f

tables = [[],[],[],[],[],[]] # Number of tables defined for test

def define_table(people):
    i = 0
<<<<<<< HEAD
    while len(people)> 0:
        if len(tables[i]) < 4:
            tables[i].append(people.pop(0))
            if len(tables[i]) == 0:
                 del tables[i]
            
        else:
            i += 1

    non_empty_tables = [table for table in tables if table]

    if len(non_empty_tables[-1]) == 1:
         non_empty_tables[-1].append(tables.pop([0][0]))


    

    for idx, table in enumerate(non_empty_tables, start=1):
            print(f"Table {idx}: {table}")
=======
    while len(people)>= 4:
        tables[i].append(people[0:4])
        del people[0:4]
        i += 1
    
    for idx, table in enumerate(tables, start=1):
        print(f"Table {idx}: {table}")
>>>>>>> 23ea96459fa6afc160c68b8811165e3d2fd8580f


def last_ones(people):
    if len(people) == 3:
        tables[i].append(people[0:3]) 

    elif len(people) == 2:
        tables[i].append(people[0:2])
    
    elif len(people) == 1:
        tables[1].append(people[0]) 

<<<<<<< HEAD
    return non_empty_tables #print les listes créées
        
print(define_table(people))
=======
    return tables #print les listes créées
  
define_table(people)
last_ones(people)

if len(my_list) >= 24:
        print(f"Sorry {remaining_persons}, the first room is full. You should rent another one.")
>>>>>>> 23ea96459fa6afc160c68b8811165e3d2fd8580f
