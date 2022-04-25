score = [433 , 562, 574, 800, 953]

#nombre de scores
n = len(score)
#initialisation de l'accumulateur
total = 0

for i in score:
    total = total+ i


print(total)

average = total/n

average = round(average)

print(average)


scores = [302 , 102, 956, 987, 931]


def int_average(numbers: list)-> int:
    """
    cette fonction renvoi un arrondi de la moyenne des nombres present dans la 
    liste passé en parametres.

    numbers : list Cette liste contient les nombres(int ou float) dont il faut
    calculer la moyenne
    return : int La fonction renvoit une moyenne arrondie au format int.
    """
    n = len(numbers)
    #initialisation de l'accumulateur
    total = 0

    for i in numbers:
        total = total+ i


    

    average = total/n

    average = round(average)

    return average

print(int_average(scores))