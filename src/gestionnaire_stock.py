from src.stock import Stock
from src.sujet import Sujet

class GestionnaireStock(Sujet):
    def __init__(self):
        super().__init__()
        self.stocks = []

    def ajouter_produit(self, produit, quantite):
        stock = Stock(produit, quantite)
        self.stocks.append(stock)
        self.notifier_observateurs(stock)

    def mettre_a_jour_stock(self, nom_produit, quantite):
        for stock in self.stocks:
            if stock.produit.nom == nom_produit:
                stock.quantite += quantite
                self.notifier_observateurs(stock)