import unittest
from unittest.mock import patch, MagicMock
from src.produit import Produit
from src.stock import Stock

class TestStock(unittest.TestCase):

    @patch('builtins.print')
    def test_affichage_stock(self, mock_print):
        mock_produit = MagicMock()
        mock_produit.nom = "Pomme"
        stock = Stock(mock_produit, 100)
        expected = "Stock de: Pomme, Quantite disponible: 100"
        stock.afficher_stock()
        mock_print.assert_called_once_with(expected)