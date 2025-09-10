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
def maximum (*args) -> float:
    max : float = args[0]
    for p in args:
        if p > max:
            max = p
    return max

print(f'maximum:{maximum(12,23,14,2.5,4)}')







