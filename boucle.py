import numbers
import random
#les types de boucles
#-while
#- do while
# #- for classique
# #- for each


# #reproduction d'une boucle for classique avec une boucle while
# #condition d'utilisation
# counter = 0
# #taille de la bouche
# limit = 10

# #tant que ..= while
#    #condition d'arret
# while counter < limit :
# #action à répéter
#     print('tour:', counter)
    
#     #increment/décrement
#     counter += 1
# # pour ... = for

#reproduction d'une boucle do while avec une boucle while
#condition d'initialisation
counter = 0
limit = 10

while True:
    #action à répéter
    print("do while:" ,counter)
    #increment/decrement
    counter += 1
    #condition de continuation
    if not (counter < limit):
        break

# for de python

for counter in range(0 ,10):
    print ('for python', counter)

mots = ['foo','bar','baz']
#methode non recommandée pour boucler 
for i in range(0, len(mots)):
    print('mot:',mots[i])

















#algo tirage de 3 nombres differents parmi 5
numbers = []
# 1er tirage
n = random.randint(1 , 5)
numbers.append(n)

#2 eme tirage
n = random.randint(1 , 5)

while True:
    n = random.randint(1 , 5)
    if n not in numbers:
        break
numbers.append(n)
print(numbers)


numbers.append(n)

print(numbers)
print(n in numbers)