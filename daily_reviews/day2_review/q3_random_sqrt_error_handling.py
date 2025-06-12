import math as m
import random as rnd


#generate random float beween 0 and 10
num = rnd.uniform(0,10)

def safe_sqrt(num):
    """Calculates the sqrt of num.
        returns the sqrt if valid,
        otherwise reutreturns an error msg str."""
    try:
        sq_root = m.sqrt(num)
        return sq_root
    except ValueError:
        return "Negative number"
    except TypeError:
        return "Wrong type!"


print(safe_sqrt(num))