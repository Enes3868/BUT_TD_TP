#premier exo du 1.2

print('plus grand nombre:')

def nbr(a: float, b: float) -> float:
    """
    Cette fonction retourne le plus grand des deux nombres réels.
    """
    return a if a > b else b

print(nbr(2.7, 2.8))
print(nbr(7.2, 7.2))




#deuxième exo
print('seuil:')





def seuil(nbr: float, maxi: float = 10) -> bool:
    """
    cette fonction indique si la valeur passée est supérieur à un seuil

    """
    return nbr if nbr > maxi else None


print(seuil(12))
print(seuil(1))
print(seuil(11))





#troisième exo
print('plus grand dune liste')


def liste(valeurs: list) -> float:
    """
    Cette fonction retourne la plus grande valeur d'une liste de nombres.

    """
    return max(valeurs)

print(liste([1, 2 , 3, 4, 5, 6]))


