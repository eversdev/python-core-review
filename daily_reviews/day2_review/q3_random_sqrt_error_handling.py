import math as m
import random as rnd

#testing to see if the modules i improted work as expcted
#print(m.sqrt(81))
#print(rnd.uniform(0,10))



#num = rnd.uniform(0,10)
#num = -9
#num = "Hi"
num = None
try:
    sq_root = m.sqrt(num)
    print(sq_root)
except ValueError:
    print("Negative number")
except TypeError:
    print("Wrong type!")


