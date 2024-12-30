import argparse
from inventory_manager import InventoryManager

def main():
    # Initialisation du parseur d'arguments
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire")
    parser.add_argument("--files", nargs="*", help="Chemins des fichiers CSV à fusionner", required=True)
    parser.add_argument("--search-name", metavar="NAME", help="Nom du produit à rechercher")
    parser.add_argument("--search-category", metavar="CATEGORY", help="Catégorie à rechercher")
    parser.add_argument("--search-price", nargs=2, metavar=('MIN', 'MAX'), help="Plage de prix à rechercher (min max)")
    parser.add_argument("--generate-report", metavar="OUTPUT", help="Générer un rapport récapitulatif dans un fichier")

    args = parser.parse_args()

    # Initialiser l'InventoryManager
    manager = InventoryManager()

    # Charger les fichiers CSV
    try:
        manager.load_csv_files(args.files)
        print("\nDonnées consolidées chargées avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement des fichiers : {e}")
        return

    # Recherche par nom
    if args.search_name:
        results = manager.search_by_name(args.search_name)
        print("\nRésultats de la recherche par nom :")
        print(results if not results.empty else "Aucun produit trouvé.")

    # Recherche par catégorie
    if args.search_category:
        results = manager.search_by_category(args.search_category)
        print("\nRésultats de la recherche par catégorie :")
        print(results if not results.empty else "Aucun produit trouvé.")

    # Recherche par plage de prix
    if args.search_price:
        try:
            min_price, max_price = map(float, args.search_price)
            results = manager.search_by_price_range(min_price, max_price)
            print("\nRésultats de la recherche par plage de prix :")
            print(results if not results.empty else "Aucun produit trouvé.")
        except ValueError:
            print("Erreur : Les prix minimum et maximum doivent être des nombres valides.")

    # Génération d'un rapport
    if args.generate_report:
        try:
            manager.generate_report(args.generate_report)
            print(f"Rapport généré dans : {args.generate_report}")
        except Exception as e:
            print(f"Erreur lors de la génération du rapport : {e}")

if __name__ == "__main__":
    main()
