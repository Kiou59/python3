from http import client
from unittest import result


texte = "foo bar baz"
splitted_text = texte.split(' ')

print(splitted_text)
print(len(splitted_text))
print(splitted_text[0])
print(splitted_text[1])
print(splitted_text[2])
#print(splitted_text[3]) = erreur

splitted_text.append(123)
print(splitted_text)

#[start:end:step]
#start inclus
#end exclu
result = splitted_text[0 : 2]
print(result)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed laoreet scelerisque est, sed finibus nulla convallis et. Aliquam est diam, bibendum et leo at, viverra blandit libero. In blandit pharetra dui in tincidunt. Praesent lobortis lacus sed metus fringilla posuere. Nulla facilisi. Etiam augue leo, finibus ut lectus at, luctus egestas mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris mauris nunc, consectetur ac egestas eget, ultrices vel arcu. Etiam molestie leo vel nisl porta, a aliquet sem lobortis. Nullam at enim malesuada, bibendum eros at, pharetra tortor. Duis hendrerit metus ut turpis dapibus facilisis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris laoreet vitae nisl eget pulvinar. In erat nunc, finibus in laoreet eget, interdum sed justo."
my_list = text.split(',')
text = ''.join(my_list)
print(text)
my_list = text.split('.')
text = ''.join(my_list)
print(text)
my_list = text.split(' ')

print(my_list)
print(len(my_list))
#tout les element de l'index 3 inclu a l'index 7 exclu
partial_list = my_list[3 : 7]
print(partial_list)
#tout les element de l'index 3 inclu à l'index 7 exclu avec un pas de 2
partial_list = my_list[3 : 7 : 2]
print(partial_list)
#tous les element de l'index 7 inclu à l'index 3 exclu
#partial_list = my_list[3 : 7]
#ne fonctionne pas: l'index start doit etre < à l'index end
start = 7
end= 3
if start>=end:
    start, end = end, start
print(start)
partial_list = my_list[-7 : -3]
print(partial_list)

#exo
#récuperer dans my_liste les mot de l'index 35 à 49 inclu
partial_list = my_list[35:50]
print(partial_list)

#afficher le numéro du dernier index
index_end = len(my_list) -1
print(index_end)
last_index=len(my_list)

#récupérer un mot sur 2 de l'index 0 au dernier index 
partial_list = my_list[0 : last_index : 2]
print(partial_list)

#4
partial_list = my_list[0:last_index:3]
partial_list2 = my_list [1:last_index:3]
partial_list3 = my_list[2 :last_index: 3]
print(partial_list)
print(partial_list2)
print(partial_list3)
#tous les elements
#caleurs par defaut :
# -start = 0
# -end = len()
# -step = 1
result = my_list[::]#copie de tout les element

#copie de tout les element en ordre inverse
result = my_list[::-1]
#copie de tous les elements à partir de start jusqu'à la fin
start=3
result= my_list[start :]

#copie de tous les éléments du début jusqu'à end
end = 10
result = splitted_text[:end]

list = []
# list.append()
#equivalent d'un push
#mode pile
list.append("foo")
list.append(214)
list.append(3.14)
print(list)
last_element = list.pop()
print(last_element)
print(list)
#mode file
list = ["toto", "titi", "tata", "tutu"]
client = list.pop(0)
print(list)
print(client)

list.insert(0 , 'mémé')
print(list)

#concatenation de liste
list_a = ['a','b','c']
list_b = [1 , 2 , 3 ]

list_c = list_a + list_b
print(list_c)

#fusion de listes (modification de l'originale)
list_a.extend(list_b)
print(list_a)

