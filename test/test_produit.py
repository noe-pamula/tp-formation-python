import unittest
from unittest.mock import patch
from src.produit import Produit

class TestProduit(unittest.TestCase):

    @patch('builtins.print')
    def test_affichage_produit(self, mock_print):
        produit = Produit("Pomme", 1.5)
        expected = "Produit: Pomme, Prix: 1.5"
        produit.afficher_details()
        mock_print.assert_called_once_with(expected)