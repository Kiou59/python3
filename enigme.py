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

# squares = [i**2 for i in range(1.100)]

# 17. Un cryptarithme est une opération dans laquelle chaque
# chiffre a été remplacé par une lettre. Une même lettre représente tou-
# jours le même chiffre, deux lettre différentes représentent deux chiffres
# différents et aucun nombre ne peut commencer par un zéro. La figure 7
# montre un exemple de cryptarithme.

#   NEUF
# +   UN
# +   UN
# ------
#   ONZE
# Figure 7 - Cryptarithme

# À partir de cette addition en lettres, retrouver celle en chiffre.
# n<8
# u>3
# n= range(1,9)
# e= range(1,10)
# u= range(1,10)
# f= range(1,10)
# z= range(1,10)
# o=range(2,10)
# onze= range(2111,10000)


for n in range(1,9):
    for e in range(1,10):
        for u in range(1 , 10):
            for f in range(1 , 10):
                    if (n*1000 + e*100 +u*10 +f)+((u*10+n)*2) in range(2111,10000) is True:
                        print((n*1000 + e*100 +u*10 +f)+((u*10+n)*2))
                        
for a in range(5,16):
    for b in range(5,16):
        if b!=a:
            for c in range(5,16):
                if c!=a and b!=c:
                    for d in range(5,16):
                        if d!=a and d!=b and d!=c:
                            for e in range(5,16):
                                if e!=a and e!=b and e!=c and e!=d:
                                    for f in range(5,16):
                                        if f!=a and f!=b and f!=c and f!=d:
                                            for g in range(5,16):
                                                if g!=a and g!=b and g!=c and g!=d and g!=f:
                                                    for h in range(5,16):
                                                        if h!=a and h!=b and h!=c and h!=d and h!=f and h !=g:
                                                            if (a+b+1+c)==(a+d+e+2) and(a+b+1+c)==(a+4+f+3) and (a+4+f+3)==(d+4+g+h):
                                                                print(a, b ,c ,d, e,f,g,h)
                                                                print(a+b+1+c)