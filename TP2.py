"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

import csv
import os
from datetime import datetime
from typing import Dict, Union, List


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


def elapsed_days(date: str) -> int:
    given_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.now()
    return (current_date - given_date).days


##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

library: Dict[str, Union[Dict[str, Union[str, int]], List[str]]] = {}
add_collection(library, "collection_bibliotheque.csv")
print(f' \n Bibliotheque initiale : {library} \n')

##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

add_collection(library, "nouvelle_collection.csv", log=True)

##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

modifications = [
    cote for cote, book in library.items()
    if book["auteur"] == "William Shakespeare"
]
for cote in modifications:
    new_cote = cote.replace("S", "WS")
    library[new_cote] = library.pop(cote)
print(f' \n Bibliotheque avec modifications de cote : {library} \n')

##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

borrows: Dict[str, str] = {}
with open("emprunts.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue
        cote, date = row
        borrows[cote] = date

for cote, book in library.items():
    title, author, year = book.values()
    library[cote]["emprunts"] = "emprunté" if cote in borrows else "disponible"
    library[cote]["date_emprunt"] = borrows.get(cote, "N/A")

print(f' \n Bibliotheque avec ajout des emprunts : {library} \n')

##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

lost_books = []
for cote, book in library.items():
    title, author, year, borrow_status, borrow_date = book.values()
    elapsed_late = 0 if borrow_status != "emprunté" else max(elapsed_days(borrow_date) - 30, 0)
    if elapsed_late > 365:
        fee = 0
        lost_books.append(cote)
    else:
        fee = min(elapsed_late * 2, 100)
    library[cote]["frais_retard"] = fee
    if fee > 0:
        print(f"Livre '{cote}' en retard: frais de {fee}$")
library["livres_perdus"] = lost_books

print(f' \n Bibliotheque avec ajout des retards et frais : {library} \n')
