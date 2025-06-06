# openspace-project

### Structure ideas

Create a Parent class openspace():
    1. Define a method wich would call the file
    2. Define the needs

Child class table
    1. Tables are created depending on the needs 
    2. Limit the number of tables to 7

Child class seats
    1. Function 1 : randomly attributes the people to the tables
    
                condition : 1 person cannot sit alone
                if there are more than 28 people in the list:
                    we have to redirect the remaining people to another room
                        print list of the names "Sorry, you have to book another room"
    
Define list of the 6 tables
 - Function wich randomly attributes elements in a list
 Make a condition : the list should not have more than 4 people

Function 