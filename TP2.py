"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

import csv

##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

bibliotheque = {}

with open("collection_bibliotheque.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        title, author, year, cote = row
        bibliotheque[cote] = {
            "titre": title,
            "auteur": author,
            "date_publication": year
        }

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

# TODO : Écrire votre code ici






##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

# TODO : Écrire votre code ici







##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

# TODO : Écrire votre code ici







##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

# TODO : Écrire votre code ici
