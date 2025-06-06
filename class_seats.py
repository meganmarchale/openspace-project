import random

people = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Yves", "Preeti",  "Aida", "joseph"]
random.shuffle(people)
#print(people)


tables = [[],[],[],[],[],[]] # Number of tables defined for test

def define_table(people):
    i = 0
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

       

       

    return non_empty_tables #print les listes créées
        
print(define_table(people))
