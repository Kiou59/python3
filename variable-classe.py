class Chaise:
    nombre_pieds =4

    def __init__(self, couleur:str):
        self.couleur=couleur


chaise1=Chaise('noir')
chaise2=Chaise('rouge')
Chaise.nombre_pieds=3
chaise1.couleur='blanc'


print('chaise1 nombrepieds:',chaise1.nombre_pieds)
print('chaise1 couleur:',chaise1.couleur)
print('chaise2 nombrepieds:',chaise2.nombre_pieds)
print('chaise2 couleur:',chaise2.couleur)
print('Chaise.nombrepieds',Chaise.nombre_pieds)