import random

# affichez les nombres de 100 à 999 avec une bouche for
# affichez les nombres de 0 à 20 qui sont multiple de 3
#affichez les nombres de 10 à 1 à rebour
#info la fonction range prend le pas en paramettre
count = range(100, 1000)

for i in count:
    print(i)

count = range(0, 21,3)

for i in count:
    print(i)

count = range(10 , 0 ,-1)

for i in count:

    print(i)

count = range(0 , 21)
for i in count:
    if  i%3 == 0:
        print(i)

```# algo : tirage de 2 nombres différents parmi 5
numbers = []

# 1er tirage
n = random.randint(1, 5)
numbers.append(n)

# 2ème tirage
while len(numbers)<4:
    n = random.randint(1, 5)
    if n not in numbers:
        numbers.append(n)

        
print(numbers)```