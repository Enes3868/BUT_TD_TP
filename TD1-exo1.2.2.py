def seuil(nbr: float, maxi: float = 10) -> bool:
    """
    cette fonction indique si la valeur passée est supérieur à un seuil

    """
    return nbr if nbr > maxi else None


print(seuil(12))
print(seuil(1))
print(seuil(11))