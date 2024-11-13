from src.produit import Produit
from src.stock import Stock

banane = Produit("Banane", 12)
orange = Produit("Orange", 10)
framboise = Produit("Framboise", 15)

banane.afficher_details()
orange.afficher_details()    
framboise.afficher_details()

stock_banane = Stock(banane, 100)
stock_orange = Stock(orange, 150)
stock_framboise = Stock(framboise, 550)

stock_banane.afficher_stock()
stock_orange.afficher_stock()
stock_framboise.afficher_stock()
