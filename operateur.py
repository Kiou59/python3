# + - * /
from operator import truediv
import random


result = 123 + 4.14
print(result)
result = (1 + 3)*3
print(result)

# // % **
#division entiere
result = 1//3
print(result)
#modulo
result = 10%3
print(result)
#puissance
#dans certains languages c'est ^, pow()
result = 3**2
print(result)
# racine
result = 9 **(1/2)
print(result)

#operateur composés
number = 42
number += 1


#operateur booleen and
result = True and True #true
result = False and True #false
result = True and False #false
result = False and False #false

# s'il n'y a que des and l'order n'est pas important
result = True and False and True and False #false

# operateut boleen or
result = True or True # true
result = True or False # true
result = False or True # true
result = False or False # false
#s'il n'y a que des or l'ordre n'as pas d'importance

#operateur boleen xor
result = True ^ True # false
result = True ^ False # true
result = False ^ True # true
result = False ^ False # false

# encadrement

a=42
b=123
c=random.randint(1 , 100)

result = a < 50 <b
print(result)

result = a < c < b
print(c)
print(result)