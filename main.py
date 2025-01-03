import argparse
from inventory_manager import InventoryManager

def main():
    parser = argparse.ArgumentParser(
        description="Système de gestion d'inventaire à partir de fichiers CSV."
    )
    
    # Ajout des options en ligne de commande
    parser.add_argument(
        "--files",
        nargs="+",
        help="Chemins des fichiers CSV à charger (séparés par des espaces).",
        required=True
    )
    parser.add_argument(
        "--search-name",
        help="Rechercher un produit par nom."
    )
    parser.add_argument(
        "--search-category",
        help="Rechercher les produits par catégorie."
    )
    parser.add_argument(
        "--search-price-range",
        nargs=2,
        type=float,
        metavar=("MIN", "MAX"),
        help="Rechercher les produits dans une plage de prix (MIN MAX)."
    )
    parser.add_argument(
        "--generate-report",
        help="Générer un rapport récapitulatif exporté dans un fichier CSV.",
        metavar="OUTPUT_FILE"
    )
    parser.add_argument(
        "--show-all",
        action="store_true",
        help="Afficher tous les produits consolidés."
    )

    # Parser les arguments
    args = parser.parse_args()

    # Initialiser le gestionnaire d'inventaire
    manager = InventoryManager()

    try:
        # Charger les fichiers CSV
        manager.load_csv_files(args.files)
        print("Données consolidées chargées avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement des fichiers : {e}")
        return

    # Actions selon les options
    if args.search_name:
        results = manager.search_by_name(args.search_name)
        print("\nRésultats de la recherche par nom :")
        print(results if not results.empty else "Aucun produit trouvé.")

    elif args.search_category:
        results = manager.search_by_category(args.search_category)
        print("\nRésultats de la recherche par catégorie :")
        print(results if not results.empty else "Aucun produit trouvé.")

    elif args.search_price_range:
        min_price, max_price = args.search_price_range
        results = manager.search_by_price_range(min_price, max_price)
        print(f"\nRésultats de la recherche entre {min_price}€ et {max_price}€ :")
        print(results if not results.empty else "Aucun produit trouvé.")

    elif args.generate_report:
        try:
            manager.generate_report(args.generate_report)
            print(f"Rapport généré avec succès dans le fichier : {args.generate_report}")
        except Exception as e:
            print(f"Erreur lors de la génération du rapport : {e}")

    elif args.show_all:
        print("\nListe complète des produits consolidés :")
        print(manager.get_data() if not manager.get_data().empty else "Aucune donnée disponible.")

    else:
        print("\nAucune action spécifiée. Utilisez --help pour voir les options disponibles.")

if __name__ == "__main__":
    main()
