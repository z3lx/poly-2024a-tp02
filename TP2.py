# Commit history available: https://github.com/z3lx/poly-2024a-tp02

import copy
import csv
import os
from datetime import datetime
from typing import Dict, Union, List

Library = Dict[str, Union[Dict[str, Union[str, int]], List[str]]]


def library_add_collection(
    library: Library,
    file_path: str,
    skip_first_line: bool = True,
    log: bool = False
) -> Library:
    if not os.path.exists(file_path):
        print(f"Le fichier '{file_path}' n'existe pas.")
        return {}

    new_library = copy.deepcopy(library)
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if skip_first_line and reader.line_num == 1:
                continue

            title, author, year, cote = row

            if cote in new_library:
                status_message = (
                    f"Le livre {cote} ---- "
                    f"{title} par {author} ---- "
                    f"est déjà présent dans la bibliothèque"
                )
            else:
                new_library[cote] = {
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
    return new_library


def library_select(
    library: Library,
    title: str = None,
    author: str = None,
    year: str = None
) -> List[str]:
    return [
        cote for cote, book in library.items()
        if (title is None or book["titre"] == title) and
           (author is None or book["auteur"] == author) and
           (year is None or book["date_publication"] == year)
    ]


def library_update_cote(
    library: Library,
    selection: List[str]
) -> Library:
    new_library = copy.deepcopy(library)
    for cote in selection:
        new_cote = cote.replace("S", "WS", 1)
        new_library[new_cote] = new_library.pop(cote)
    return new_library


def load_borrows(
    file_path: str,
    skip_first_line: bool = True
) -> Dict[str, str]:
    borrows: Dict[str, str] = {}
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if skip_first_line and reader.line_num == 1:
                continue
            cote, date = row
            borrows[cote] = date
    return borrows


def library_add_borrows(
    library: Library,
    borrows: Dict[str, str]
) -> Library:
    new_library = copy.deepcopy(library)
    for cote, book in new_library.items():
        status = "emprunté" if cote in borrows else "disponible"
        new_library[cote]["emprunts"] = status
        new_library[cote]["date_emprunt"] = borrows.get(cote, "N/A")
    return new_library


def elapsed_days(date: str) -> int:
    given_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.now()
    return (current_date - given_date).days


def library_add_fees(
    library: Library,
    log: bool = False
) -> Library:
    new_library = copy.deepcopy(library)
    lost_books = []
    for cote, book in new_library.items():
        title, author, year, borrow_status, borrow_date = book.values()

        elapsed_late = 0 if borrow_status != "emprunté" \
            else max(elapsed_days(borrow_date) - 30, 0)

        if elapsed_late > 365:
            fee = 0
            lost_books.append(cote)
        else:
            fee = min(elapsed_late * 2, 100)

        new_library[cote]["frais_retard"] = fee
        if fee > 0 and log:
            print(f"Livre '{cote}' en retard: frais de {fee}$")
    new_library["livres_perdus"] = lost_books
    return new_library


def main() -> None:
    ############################################################################
    # PT1 : Création du système de gestion et ajout d'une collection actuelle  #
    ############################################################################

    library = library_add_collection({}, "collection_bibliotheque.csv")
    print(f" \n Bibliotheque initiale : {library} \n")

    ############################################################################
    # PT2 : Ajout d'une nouvelle collection à la bibliothèque                  #
    ############################################################################

    library = library_add_collection(library, "nouvelle_collection.csv", log=True)

    ############################################################################
    # PT3 : Modification de la cote de rangement d'une sélection de livres     #
    ############################################################################

    selection = library_select(library, author="William Shakespeare")
    library = library_update_cote(library, selection)
    print(f" \n Bibliotheque avec modifications de cote : {library} \n")

    ############################################################################
    # PT4 : Emprunts et retours de livres                                      #
    ############################################################################

    borrows = load_borrows("emprunts.csv")
    library = library_add_borrows(library, borrows)
    print(f" \n Bibliotheque avec ajout des emprunts : {library} \n")

    ############################################################################
    # PT5 : Livres en retard                                                   #
    ############################################################################

    library = library_add_fees(library, log=True)
    print(f" \n Bibliotheque avec ajout des retards et frais : {library} \n")


if __name__ == "__main__":
    main()
