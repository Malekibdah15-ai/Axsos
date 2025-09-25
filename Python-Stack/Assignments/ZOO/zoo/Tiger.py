from Animal import Animal

class Tiger(Animal):
    def __init__(self, name, age, health_level, happiness_level, hieght):
        super().__init__(name, age, health_level, happiness_level)
        self.hieght = hieght
        
        
        
  
    
    
    
    def feed(self,):
         healthincrease = 20
         happinessincrease = 20
         
         if self.length < 70 :
             super().feed(healthincrease, happinessincrease).display_info()