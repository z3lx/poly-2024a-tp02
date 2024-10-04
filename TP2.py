"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

import csv
import os
from typing import Dict


def add_collection(
    library: Dict[str, Dict[str, str]],
    collection_path: str,
    skip_first_line: bool = True,
    log: bool = False
) -> None:
    if not os.path.exists(collection_path):
        print(f"Le fichier '{collection_path}' n'existe pas.")
        return

    with open(collection_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if skip_first_line and reader.line_num == 1:
                continue

            title, author, year, cote = row

            if cote in library:
                status_message = (
                    f"Le livre {cote} ---- "
                    f"{title} par {author} ---- "
                    f"est déjà présent dans la bibliothèque"
                )
            else:
                library[cote] = {
                    "titre": title,
                    "auteur": author,
                    "date_publication": year
                }
                status_message = (
                    f"Le livre {cote} ---- "
                    f"{title} par {author} ---- "
                    f"a été ajouté avec succès"
                )

            if log:
                print(status_message)


##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

bibliotheque: Dict[str, Dict[str, str]] = {}
add_collection(bibliotheque, "collection_bibliotheque.csv")
print(f' \n Bibliotheque initiale : {bibliotheque} \n')

##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

add_collection(bibliotheque, "nouvelle_collection.csv", log=True)

##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

modifications = [
    cote for cote, book in bibliotheque.items()
    if book["auteur"] == "William Shakespeare"
]
for cote in modifications:
    new_cote = cote.replace("S", "WS")
    bibliotheque[new_cote] = bibliotheque.pop(cote)
print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')

##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

# TODO : Écrire votre code ici







##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

# TODO : Écrire votre code ici
