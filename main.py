from inventory_manager import InventoryManager

def main():
    print("Bienvenue dans le système de gestion d'inventaire !")
    
    # Demander les fichiers CSV à l'utilisateur
    file_input = input("Entrez les chemins des fichiers CSV à fusionner (séparés par des virgules) : ")
    file_paths = [file.strip() for file in file_input.split(",")]

    # Initialiser l'InventoryManager
    manager = InventoryManager()
    
    try:
        # Charger et fusionner les fichiers CSV
        manager.load_csv_files(file_paths)
        print("\nDonnées consolidées chargées avec succès.")
    except Exception as e:
        print(f"Erreur : {e}")
        return

    while True:
        print("\nOptions disponibles :")
        print("1. Rechercher un produit")
        print("2. Afficher toutes les données")
        print("3. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            column = input("Entrez le nom de la colonne pour la recherche (ex. 'Nom du produit') : ")
            value = input(f"Entrez la valeur à rechercher dans la colonne '{column}' : ")
            try:
                results = manager.search(column, value)
                print("\nRésultats de la recherche :")
                print(results if not results.empty else "Aucun résultat trouvé.")
            except Exception as e:
                print(f"Erreur : {e}")
        elif choice == "2":
            print("\nDonnées consolidées :")
            print(manager.get_data())
        elif choice == "3":
            print("Merci d'avoir utilisé le système de gestion d'inventaire. À bientôt !")
            break
        else:
            print("Option invalide, veuillez réessayer.")
            
if __name__ == "__main__":
    main()