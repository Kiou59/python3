import numbers
from timeit import default_timer as timer
start = timer()
end = timer()
duration = end - start
print('duration:',duration)


for i in range(1000, 9999):
    if (int(i**(1/2)) == (i**(1/2))) and (int((i//100)**(1/2)))== ((i//100)**(1/2)) and int((i%100)**(1/2)) ==(i%100)**(1/2) and i%100 !=0:
        print (i)


# for i in range(1000, 9999):
#     if int(i**(1/2)) == (i**(1/2)) :
#         if int(((i//100)**(1/2)))== ((i//100)**(1/2)) and int((i%100)**(1/2)) ==(i%100)**(1/2):
#             print(i)

#exo 01
numbers = [4 , 10 , 42, 3.14]
my_list = []

while True:
    number = numbers.pop()
    my_list.append(number)

    if len(numbers)==0:
        break


# resultats = 0
# #carré de deux chiffres : 4 a 9
# carres_2_chiffres=[]

# for i in range(4 , 10):
#     carres_2_chiffres.append(i **2)

# #carré de 4 chiffres : 32 à 99
# carres_4_chiffres = []

# for i in range(32 , 100):
#     carres_4_chiffres.append(i ** 2)

# #construisons des nombres à 4 chiffres

# for i in carres_2_chiffres:
#     for j in carres_2_chiffres:
#         nombre = i*100 + j

#         if nombre in carres_4_chiffres:
#             resultats.append(nombre)

L1 = [ n**2 for n in range (3163,10000)] 

for i in L1:
    if (i%100) == (i//100)+1:
        print (L1[i])


3163**2
9999 **2

for i in range(3163,9999+1):
    carre = i ** 2 
    premier = carre // 10000
    dernier = carre % 10000
    if dernier == premier + 1:
        print(i)
# un artilleur dispose de boulets de canon répartis dans un carré parfait. 
#Pour reduire l'encombrement au sol, l'artilleur reussit à empliler ses boulets
#pour former une belle pyramide à base carrée.

squares = [i**2 for i in range(1.100)]

