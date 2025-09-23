
import random
def randInt(min=0   , max= 100  ):
    range_size = max- min
    num = random.random() * range_size + min
    return num
print(randInt())             
print(randInt(max=50))         
print(randInt(min=50))        
print(randInt(min=50, max=500))  