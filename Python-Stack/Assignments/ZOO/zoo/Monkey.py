from Animal import Animal

class Monkey(Animal):
    def __init__(self, name, age, health_level, happiness_level, weight):
        super().__init__(name, age, health_level, happiness_level)
        self.weight = weight
        
        
    
    
    
    
    
    def feed(self):
         healthincrease = 50
         happinessincrease = 50
         
         if self.weight >= 50:
             super().feed(healthincrease, happinessincrease).display_info()
     