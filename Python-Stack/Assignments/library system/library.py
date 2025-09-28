class library:
    def __init__(self, title, ):
        self.title = title
        self.available = True
        
    
        
    def Borrowing_Items(self):
        if self.available:
            self.available = False
            print(f"{self.title} have been borrowed")
            return self
        else:
            print(f"{self.title} is avalibale")
            
        
    def Returning_Items(self):
        if self.available:
            self.available = True
            print(f"{self.title} returned items")
        
    
    def Check_Availability(self):
        if self.available:
            self.available = True
            print(f"{self.title} is available")
        else:
            print(f"{self.title} not avalibale")
    
    def Late_Fee_Calculation(self, days_late):
        return days_late * 1.3
   
    
    def Overdue_Notification(self, notes):
        return notes
        
class Book(library):
       def Late_Fee_Calculation(self, days_late):
        return days_late * 1.3
   
     
class Dvd(library):
     def Late_Fee_Calculation(self, days_late):
        return days_late * 2.3
       
   
         
class Magazine(library):
       def Late_Fee_Calculation(self, days_late):
        return days_late * 0.3
   
   
book1 = Book("war and peace")
book1.Borrowing_Items()
