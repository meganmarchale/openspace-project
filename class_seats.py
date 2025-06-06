import random

people = ["Hajer", "Charly", "Choti", "Megan", "Moussa", "Yves", "Preeti", "Nadiya", "Aida", "Augustin", "Klebert", "Marc", "Sofia", "Younes", "Kenny", "Floriane", "Jordi", "Alberto", "Fang", "Caterina", "Yassine", "Dragos", "Hanieh", "Mengstu"]
x = 5 # Number of tables defined for test

def define_table(people):
    if len(people) >= 2:
        table_1 = random.sample(people, 4)
        people = [list[set(people) - set(table_1)]] ### Modify "table1 by element of a list created in class tables ??"
        return f"{table_1} can sit in table 1" #prints a list of 4 persons

#Call the function x times depending on the needs defined ? 

def repeat_define_table(define_table, x):
    for i in range(x): define_table(people)

repeat_define_table(x, define_table)
print(define_table(people))

print(f"If your name appears in this list, you'll have to book another room: {people}")
