
from Animal import Animal
from Lion import Lion
from Monkey import Monkey
from Tiger import Tiger


class Zoo:
    def __init__(self, name):
        self.animals = []
        self.name = name
        
    def add_Lion(self, name, age, health_level, happiness_level, length):
        self.animals.append( Lion(name, age, health_level, happiness_level, length))
        
    
    def add_Tiger(self, name, age, health_level, happiness_level, hieght):
        self.animals.append( Tiger( name, age, health_level, happiness_level, hieght))
        
    def add_Monkey(self, name, age, health_level, happiness_level, weight):
        self.animals.append( Monkey( name, age, health_level, happiness_level, weight))
        
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        print(len(self.animals))
        for animal in self.animals:
            print(animal.display_info())
            
            
zoo1 = Zoo("peter")
zoo1.add_Lion("sampa","10",30,40,180)
zoo1.add_Tiger("karlo","20",50,60,130)
zoo1.add_Monkey("peter","5",10,9,40)
zoo1.print_all_info()
