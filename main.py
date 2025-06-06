import random
class OpenSpace:
    """
    This class uploaded file colleague.csv and randomly define the number of person 
    to distribute in each table
    """
    def __init__(self, filename = "./colleagues.csv"):
        self.filename = filename
        self.my_list = []
        
        
        
    def uploaded_file(self):
        """
        This method upload file and add the content in a list called my_list
        """
        
        with open(self.filename, "r") as input_file:
            lines = input_file.readlines()
            self.my_list= [line.strip() for line in lines]
            

        return self.my_list
        
    
    def random_list(self):
        """
        This method create a new randomly list by a given number of person 
        in my_list
        """
        
        #random.shuffle(self.my_list)
        self.people = random.sample(self.my_list, 24)
        print(self.people)
        self.remaining_persons = list[set(self.my_list) - set(self.people)]

        if len(self.my_list) >= 25:
            print(f"Sorry {self.remaining_persons}, the first room is full. You should rent another one.")

        return self.my_list
        
    def create_table(self):
        """
        This method create table according to the way that any table should not have 
        more than 4 persons and should have more than one person
        """
        #print(self.my_list)
        self.tables = [[], [], [], [], [], []]
        #print(self.tables)
        i = 0

        while self.my_list:
            if len(self.tables[i]) <= 4:  # Max 4 per table
                self.tables[i].append(self.my_list.pop(0))
            i = (i + 1) % len(self.tables)  # Go to next table circularly

        

        # Print the tables
    def define_table(self):
        self.tables = [[], [], [], [], [], []]
        i = 0
        while len(self.people)>= 4:
            self.tables[i].append(self.people[0:4])
            del self.people[0:4]
            i += 1
        
        for idx, table in enumerate(self.tables, start=1):
            print(f"Table {idx}: {table}")


    def last_ones(self):
        if len(self.people) == 3:
            self.tables[i].append(self.people[0:3]) 

        elif len(self.people) == 2:
            self.tables[i].append(self.people[0:2])
        
        elif len(self.people) == 1:
            self.tables[1].append(self.people[0]) 

        return self.tables #print les listes créées
        
   
    
            
test = OpenSpace()

test.uploaded_file()
test.random_list()
#test.create_table()
print(test.define_table())
test.last_ones()

