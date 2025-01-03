import unittest
import pandas as pd
import os
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        """Configuration avant chaque test"""
        self.manager = InventoryManager()
        self.sample_data = pd.DataFrame({
            "Id": [1, 2, 3],
            "Nom du produit": ["carottes", "pommes", "bananes"],
            "Quantite": [300, 200, 100],
            "Prix": [0.82, 1.5, 1.6],
            "Categorie": ["legume", "fruit", "fruit"]
        })
        self.manager.data = self.sample_data
        self.test_csv = "test_inventory.csv"

    def tearDown(self):
        """Nettoyage après chaque test"""
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_load_csv_files(self):
        """Test du chargement et de la fusion des fichiers CSV"""
        # Créez un fichier CSV temporaire
        with open(self.test_csv, "w", encoding="utf-8") as f:
            f.write("Id;Nom du produit;Quantite;Prix;Categorie\n")
            f.write("1;carottes;300;0.82;legume\n")
            f.write("2;pommes;200;1.5;fruit\n")

        result = self.manager.load_csv_files([self.test_csv])
        self.assertEqual(len(result), 2)
        self.assertIn("carottes", result["Nom du produit"].values)

    def test_search_by_name(self):
        """Test de la recherche par nom du produit"""
        results = self.manager.search_by_name("carottes")
        self.assertEqual(len(results), 1)
        self.assertEqual(results.iloc[0]["Nom du produit"], "carottes")

    def test_search_by_category(self):
        """Test de la recherche par catégorie"""
        results = self.manager.search_by_category("fruit")
        self.assertEqual(len(results), 2)
        self.assertIn("pommes", results["Nom du produit"].values)
        self.assertIn("bananes", results["Nom du produit"].values)

    def test_search_by_price_range(self):
        """Test de la recherche dans une plage de prix"""
        results = self.manager.search_by_price_range(1.0, 1.6)
        self.assertEqual(len(results), 2)
        self.assertIn("pommes", results["Nom du produit"].values)
        self.assertIn("bananes", results["Nom du produit"].values)

    def test_generate_report(self):
        """Test de la génération de rapport"""
        output_file = "test_report.csv"
        self.manager.generate_report(output_file)
        self.assertTrue(os.path.exists(output_file))

        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Nombre total de produits", content)
        self.assertIn("Quantité totale", content)
        self.assertIn("Valeur totale des stocks", content)

if __name__ == "__main__":
    unittest.main()
