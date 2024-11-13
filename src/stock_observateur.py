
from src.observateur import Observateur

class StockObservateur(Observateur):
    def mettre_a_jour(self, stock):
        print("Stock mis à jour")
        stock.afficher_stock()