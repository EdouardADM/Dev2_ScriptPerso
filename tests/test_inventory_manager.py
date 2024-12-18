import unittest
import pandas as pd
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
        self.manager._data = self.sample_data

    def test_load_csv_files(self):
        """Test du chargement et de la fusion des fichiers CSV"""
        # Créez des fichiers CSV temporaires pour ce test si nécessaire
        pass  # Implémentation simulée

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
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Nombre total de produits", content)
        self.assertIn("Quantite_totale", content)
        self.assertIn("Valeur_totale", content)

if __name__ == "__main__":
    unittest.main()
