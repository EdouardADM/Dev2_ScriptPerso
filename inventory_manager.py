import pandas as pd
import os

class InventoryManager:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_csv_files(self, file_paths):
        """
        Charge plusieurs fichiers CSV et les fusionne en une seule base de données.
        :param file_paths: Liste des chemins des fichiers CSV.
        :return: DataFrame consolidé ou une exception en cas d'erreur.
        """
        loaded_data = []
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")

            try:
                df = pd.read_csv(file_path)
                loaded_data.append(df)
            except Exception as e:
                raise ValueError(f"Erreur lors du chargement du fichier '{file_path}': {e}")

        # Vérification des colonnes
        column_sets = [set(df.columns) for df in loaded_data]
        if not all(columns == column_sets[0] for columns in column_sets):
            raise ValueError("Les colonnes des fichiers CSV ne sont pas cohérentes.")

        # Fusionner les fichiers
        self.data = pd.concat(loaded_data, ignore_index=True)
        return self.data

    def get_data(self):
        """
        Retourne les données consolidées.
        """
        return self.data

    '''
    # Exemple d'utilisation si besoin
    def main():
        manager = InventoryManager()
        try:
            files = ["stocks_department1.csv", "stocks_department2.csv"]
            consolidated_data = manager.load_csv_files(files)
            print("Données consolidées :\n", consolidated_data.head())
        except Exception as e:
            print(f"Erreur: {e}")

    if __name__ == "__main__":
        main()
    '''
    def search(self, column, value):
        """
        Recherche des produits dans l'inventaire selon un critère.
        :param column: Nom de la colonne (ex. 'Nom du produit', 'Catégorie').
        :param value: Valeur à rechercher (ex. 'Produit A', 'Catégorie 1').
        :return: DataFrame des résultats de recherche.
        """
        if column not in self.data.columns:
            raise ValueError(f"La colonne '{column}' n'existe pas dans les données.")
        
        # Filtrer les données selon la valeur spécifiée
        results = self.data[self.data[column].str.contains(value, case=False, na=False)]
        return results