# Dev2_ScriptPerso
# Système de Gestion d'Inventaire

## Description du projet

Le Système de Gestion d'Inventaire est un programme en ligne de commande permettant de :

- Consolider plusieurs fichiers CSV contenant des données d'inventaire en une base unique.
- Rechercher rapidement des informations sur les produits par **nom**, **catégorie**, ou **prix**.
- Afficher toutes les données consolidées.
- Générer un rapport récapitulatif exportable en fichier CSV, contenant des statistiques globales et par catégorie.

## Fonctionnalités principales

1. Consolider plusieurs fichiers CSV en une base unique.
2. Rechercher rapidement des informations :
   - Par nom de produit.
   - Par catégorie.
   - Par prix exact ou dans une plage de prix.
3. Afficher les données consolidées.
4. Générer un rapport récapitulatif exportable.

---

## Prérequis

- **Python 3.x** doit être installé sur votre système.
- Bibliothèques Python nécessaires :
  - `pandas`

Pour installer `pandas`, utilisez la commande suivante :

```bash
pip install pandas
```

---

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers nécessaires.
2. Assurez-vous que tous les fichiers sont dans le même dossier.
3. Placez vos fichiers CSV à analyser dans un dossier nommé `data`.

---

## Utilisation

Pour lancer le programme, exécutez le fichier `main.py` :

```bash
python main.py
```

### Options disponibles

Lorsque le programme est lancé, vous pouvez choisir parmi les options suivantes :

```
1. Rechercher par nom du produit
2. Rechercher par catégorie
3. Rechercher par prix exact
4. Rechercher dans une plage de prix
5. Afficher toutes les données
6. Générer un rapport récapitulatif exportable
7. Quitter
```

---

## Structure du projet

Voici la structure des fichiers du projet :

```
.
├── inventory_manager.py   # Classe pour gérer les opérations d'inventaire
├── main.py                # Fichier principal pour exécuter le programme
├── README.md              # Documentation
├── data/                  # Dossier pour les fichiers CSV d'entrée
└── tests/                 # Dossier pour les tests unitaires
```

---

## Exemple de fichier CSV

Voici un exemple de format attendu pour les fichiers CSV :

```csv
Id;Nom du produit;Quantite;Prix;Categorie
1;carottes;300;0.82;legume
2;bananes;100;1.6;fruit
3;pommes;200;1.5;fruit
```

---

## Rapport généré

Voici un exemple de rapport récapitulatif exporté dans un fichier `rapport_recapitulatif.csv` :

```
# Rapport Récapitulatif des Stocks
Nombre total de produits : 17
Quantité totale : 1377
Valeur totale des stocks : 210.00 €

# Statistiques par catégorie
Categorie,Quantite_totale,Valeur_totale
boeuf,50,210.0
fruit,480,150.0
legume,675,240.0
```

---

## Tests

Des tests unitaires peuvent être lancés pour vérifier le bon fonctionnement des méthodes dans `inventory_manager.py`.

Pour exécuter les tests :

```bash
python -m unittest discover tests
```

---

## Licence

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).