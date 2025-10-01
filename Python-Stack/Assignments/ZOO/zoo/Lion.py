from Animal import Animal

class Lion(Animal):
    
    def __init__(self, name, age, health_level, happiness_level, length):
        super().__init__(name, age, health_level, happiness_level)
        self.length = length
        
    
   
    
    def feed(self):
        healthincrease = 30
        happinessincrease = 30
         
        if self.length >= 70:
            super().feed(healthincrease, happinessincrease).display_info()
     
malek = Lion()