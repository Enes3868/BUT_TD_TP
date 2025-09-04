class Tasse:
    attributmatiere : str = "ceramique"
    def __init__(self, couleur: str, contenance:int, marque:str, valeur : int):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
        self.attributmatiere = valeur

    def __str__(self):
        return f'la tasse de matière {self.attributmatiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml'

