class Tasse:
    attributmatiere : str = "ceramique"
    # Méthode init
    def __init__(self, couleur: str, contenance:int, marque:str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
    # Méthode str
    def __str__(self):
        return f'la tasse de matière {Tasse.attributmatiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml'

    # Méthode pour définir le contenu
    def ajouter_contenu(self, contenu: str):
        self.contenu = contenu

    # Méthode pour supprimer le contenu
    def boire(self):
        if hasattr(self, 'contenu'):
            del self.contenu


tasse1 = Tasse("bleue", 50, "Duralex")

"""
Affichage de la tasse

"""

print(tasse1)

"""
la tasse de matière céramique, de couleur bleue et de marque Duralex a une contenance de 50 ml
"""

""" 
Ajouter un contenu

"""
tasse1 = Tasse("bleue", 50, "Duralex")
tasse1.ajouter_contenu("thé")

print(f"{tasse1} Elle contient du {tasse1.contenu}.")
