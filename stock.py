
class Stock:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def afficher_stock(self):
        print(f"Stock de: {self.produit.nom}, Quantite disponible: {self.quantite}")