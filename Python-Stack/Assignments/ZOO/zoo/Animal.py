class Animal:
    def __init__(self, name, age, health_level, happiness_level):
            self.name = name
            self.age = age
            self.health_level = health_level
            self.happiness_level = happiness_level
            
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Health: {self.health_level}, Happiness: {self.happiness_level},"
    
    
    
    
    
    def feed(self,):
        self.health_level += 10
        self.happiness_level += 10
        
            
        
    