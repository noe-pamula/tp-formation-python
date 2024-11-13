
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher_details(self):
        print(f"Produit: {self.nom}, Prix: {self.prix}")