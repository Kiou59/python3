from ast import keyword
import random

firstname = "toto"
lastname = "pop" 
number = 2
email = firstname + '.' + lastname + str(number) + '@exemple.fr'
print(email)

new_emails = random.randint(0 ,3)

if new_emails == 0 :
    print("Vous n'avez pas de nouveaux mails")
elif new_emails == 1:
    print("Vous avez recu <strong>1</strong> nouveau mail")
else :
    print("Vous avez reçu <strong>"+ str(new_emails)+"</strong> nouveaux emails")

stock = random.randint(0 , 15)

if stock ==0:
    print("Stock épuisé")
elif stock == 1:
    print("Stock en tensoin: 1 pièce")
elif 1<stock<5 :
    print(f"Stock en tension:{stock} pieces")
elif 5<=stock<10 :
    print(f"Stock confortable:{stock} pieces")
elif 10<=stock :
    print(f"Stock en surnombre:{stock} pieces")

temperature = random.randint(10000,20000)/1000
print(temperature)

print(f"La température actuelle est de {temperature:.2f}°C")

print(f"Le  nombre tiré au hasard est {random.randint(0 , 10)}")

texte ="foo bar baz"
# len == length ==longueur

print(len(texte))
print(texte.find("banana"))
print(texte.find("baz"))

texte = "Bonjour Toto"

keyword = "Toto"

if texte.find(keyword) ==-1:
    print(f"{keyword} n'est pas présent")
else:
    print(f"{keyword} est présent")

texte = "Bnjour  Toto"
texte= texte.replace('Bnjour', 'Bonjour')
texte= texte.replace('  ',' ')
texte= texte.replace('Toto','Titi')
print(texte)