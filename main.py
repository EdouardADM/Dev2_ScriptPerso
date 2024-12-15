from inventory_manager import InventoryManager

def main():
    print("Bienvenue dans le système de gestion d'inventaire !")
    
    # Initialiser l'InventoryManager
    manager = InventoryManager()
    
    # Demander les fichiers CSV à l'utilisateur
    file_input = input("Entrez les chemins des fichiers CSV à fusionner (séparés par des virgules) : ")
    file_paths = [file.strip() for file in file_input.split(",")]

    try:
        # Charger et fusionner les fichiers CSV
        manager.load_csv_files(file_paths)
        print("\nDonnées consolidées chargées avec succès.")
    except Exception as e:
        print(f"Erreur : {e}")
        return

    while True:
        print("\nOptions disponibles :")
        print("1. Rechercher par nom du produit")
        print("2. Rechercher par catégorie")
        print("3. Afficher toutes les données")
        print("4. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            name = input("Entrez le nom (ou partie du nom) du produit à rechercher : ")
            results = manager.search_by_name(name)
            print("\nRésultats de la recherche par nom :")
            print(results if not results.empty else "Aucun produit trouvé.")
        
        elif choice == "2":
            category = input("Entrez la catégorie à rechercher : ")
            results = manager.search_by_category(category)
            print("\nRésultats de la recherche par catégorie :")
            print(results if not results.empty else "Aucun produit trouvé.")
        
        elif choice == "3":
            print("\nDonnées consolidées :")
            print(manager.get_data())
        
        elif choice == "4":
            print("Merci d'avoir utilisé le système de gestion d'inventaire. À bientôt !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
