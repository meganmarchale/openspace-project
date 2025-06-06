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
        
        random.shuffle(self.my_list)
        
        return self.my_list
        
    def create_table(self):
        """
        This method create table according to the way that any table should not have 
        more than 4 persons and should have more than one person
        """
        print(self.my_list)
        self.tables = [[], [], [], [], [], []]
        print(self.tables)
        i = 0

        while self.my_list:
            if len(self.tables[i]) <= 4:  # Max 4 per table
                self.tables[i].append(self.my_list.pop(0))
            i = (i + 1) % len(self.tables)  # Go to next table circularly

        

        # Print the tables
        for idx, table in enumerate(self.tables, start=1):
            print(f"Table {idx}: {table}")
            

        print(self.tables)


        
test = OpenSpace()
test.uploaded_file()
test.random_list()
print(test.create_table())


