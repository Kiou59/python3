import random
from tabnanny import check

# if True:
#     print("ce message sera toujours affiché(if True)")
# else:
#     print("ce message ne sera jamais affiché(if True)")

# if False:
#     print("ce message ne sera jamais affiché(if False)")
# else:
#     print("ce message sera toujours affiché(if False)")

# fruits =['banana','apple','cherry']
# if 'apple' in fruits:
#     print('il y a des pommes')
# else:
#     print('il n y a pas de pommes')
# if 'orange' in fruits:
#     print('il y a des oranges')
# else:
#     print('il n y a pas d oranges')

# is_authentificated =True

# if is_authentificated:
#     print("L'utilisateur peut acceder aux backoffice")

# user_password_in_form ='123'
# user_password_in_dtb ='abc'

# if user_password_in_form == user_password_in_dtb:
#     print("l'utilisateur peut se connecter")
# else :
#     print('mot de passe ou email incorrect')

# users_in_db = ['toto','titi','tata','tutu']
# tutu_password_in_dtb ='abc'

# username_in_form = 'tutu'
# user_password_in_form ='abc'

# if username_in_form in users_in_db and user_password_in_form == tutu_password_in_dtb:
#     print('acces aux backoffice')
# else :
#     print('mot de passe ou id incorrect')

# is_authentificated = True
# users_in_db = ['toto','titi','tata','tutu']
# tutu_password_in_dtb ='abc'

# username_in_form = 'tutu'
# user_password_in_form ='123'

# if (username_in_form in users_in_db and user_password_in_form == tutu_password_in_dtb) or is_authentificated:
#     print('acces aux backoffice')
# else :
#     print('mot de passe ou id incorrect')

# electricity = bool(random.randint(0,1))
# water = bool(random.randint(0 , 1))
# gas = bool(random.randint(0 , 1))

# print('electricity:', electricity)
# print('water:', water)
# print('gas:', gas)

# if electricity == False and water == False and gas ==False:
#     print("vous pouvez partir en weekend")
# else:
#     print("il reste des sources à couper")

#     if electricity:
#         print("coupez l'electricité")
    
#     if water:
#         print("coupez l'eau")

#     if gas:
#         print("coupez le gaz")

# if not electricity and not water and not gas :
#     print('vous pouvez partir en vacances')
# if electricity and not water and not gas:
#     print("vous devez coupez l'éléctricité avant de partir en vacances")
# if electricity and water and not gas:
#     print("vous devez couper l'éléctricité et le gas avant de partir en vacances")
# if electricity and water and gas:
#     print("vous devez couper l'eau l'élécticité et le gaz avant de partir en vacances")
# if not electricity and water and gas:
#     print("vous devez couper l'eau et le gaz avant de partir en vacances")
# if not electricity and not water and gas:
#     print("vous devez couper le gaz avant de partir en vacances")
# if not electricity and water and not gas:
#     print("vous devez couper l'eau avant de partir en vacances")
# if electricity and not water and gas:
#     print("Vous devez coupez l'éléctricité et le gaz avant de partir en vacances")

# has_cash = bool(random.randint(0 , 1))
# has_card = bool(random.randint(0 , 1))
# has_check = bool(random.randint(0 , 1))
# print('cash:', has_cash)
# print("card:", has_card)
# print('check:', has_check)

# if has_cash or has_card or has_check:
#     print("vous pouvez partir faire des courses")

#     if has_cash :
#         print("vous avez du cash")

#     if has_card:
#         print("vous avez votre carte")

#     if has_check :
#         print("vous avez votre chequier")

# else:
#     print("vous n'avez aucun moyen de paiement")

age = random.randint(0,100)
#0-5 bébé
#6-11 enfant
#12-25 ado-jeune adulte
#26-59 adulte
#60+ senior

if age <= 5 :
    print("bébé") 
elif 6 <= age <=11:
    print("enfant")
elif 12<= age <=25 :
    print("ado-jeune adulte")
elif 26 <= age <=59 :
    print("adulte")
elif age>= 60 :
    print("senior")