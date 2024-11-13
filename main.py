from src.produit import Produit
from src.stock import Stock
from src.gestionnaire_stock import GestionnaireStock
from src.stock_observateur import StockObservateur

banane = Produit("Banane", 12)
orange = Produit("Orange", 10)
framboise = Produit("Framboise", 15)

banane.afficher_details()
orange.afficher_details()    
framboise.afficher_details()

# stock_banane = Stock(banane, 100)
# stock_orange = Stock(orange, 150)
# stock_framboise = Stock(framboise, 550)

# stock_banane.afficher_stock()
# stock_orange.afficher_stock()
# stock_framboise.afficher_stock()


gestionnaire_stock = GestionnaireStock()
gestionnaire_stock.ajouter_observateur(StockObservateur())
gestionnaire_stock.ajouter_produit(banane, 100)
gestionnaire_stock.ajouter_produit(orange, 150)
gestionnaire_stock.ajouter_produit(framboise, 550)


gestionnaire_stock.mettre_a_jour_stock("Banane", 50)
gestionnaire_stock.mettre_a_jour_stock("Orange", 50)
gestionnaire_stock.mettre_a_jour_stock("Framboise", 50)
