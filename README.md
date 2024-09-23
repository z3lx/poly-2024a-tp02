# TP02 : Système de gestion de livres pour une bibliothèque :books:

## Directives
:alarm_clock: Date de remise : Le 6 octobre 2024

:mailbox_with_mail: À remettre sur Moodle

## Introduction
L'objectif de ce travail pratique est de développer un système de gestion d'une collection de livres dans une bibliothèque. Le système de gestion devra permettre aux utilisateurs de gérer les emprunts et les retours de livres, d'ajouter des nouveaux livres à la collection, et autres fonctionnalités essentielles pour la gestion efficace de la bibliothèque.

Le travail pratique vise principalement à :

- :ballot_box_with_check: Maîtriser l'utilisation des structures de contrôle, telles que les structures conditionnelles ('if', 'else', etc.) et les structures de répétition ('for', 'while', etc.).
- :ballot_box_with_check: Maîtriser l'utilisation des structures de données, telles que les listes, les dictionnaires, les tuples et les ensembles.
- :ballot_box_with_check: Appliquer ces structures de contrôle et de données pour développer une application pratique, c'est-à-dire un système de gestion de bibliothèque.

## Instructions

### Partie 1 : Création du système de gestion et ajout de la collection actuelle (2 points)
Vous avez à votre disposition la liste des livres de la collection actuelle de la bibliothèque, disponible dans le fichier `collection_bibliotheque.csv`. Ce fichier contient les informations suivantes pour chaque livre :
- Le titre du livre
- L'auteur
- La date de publication
- La cote de rangement

La cote de rangement, composée d'une lettre suivie de trois chiffres, est unique à chaque livre et permet aux employés de la bibliothèque de les localiser facilement.

Dans cette première partie du laboratoire, vous devez créer un dictionnaire Python appelé `bibliotheque` pour gérer la collection de livres. Ce dictionnaire doit utiliser la cote de rangement comme clé principale. Chaque entrée de ce dictionnaire doit inclure les informations suivantes :
- `titre`
- `auteur`
- `date_publication`

Pour ce faire, vous devez d'abord faire la lecture du fichier `collection_bibliotheque.csv` pour pouvoir y extraire l'information contenue au sujet des livres (le titre, l'auteur, etc.). Indice : utilisez le module [csv](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html) intégré dans Python. 

Par la suite, vérifiez que votre dictionnaire `bibliotheque` contienne correctement les informations du fichier `collection_bibliotheque.csv` en affichant son contenu avec `print(f' \n Bibliotheque initiale : {bibliotheque} \n')`. 

### Partie 2 : Ajout d'une nouvelle collection à la bibliothèque (3 points)
La bibliothèque a fait l'achat d'une nouvelle collection de livres. Cette nouvelle collection est contenue dans le fichier `nouvelle_collection.csv`. 

Ajoutez les livres de cette nouvelle collection au système de gestion (c'est-à-dire, dans le dictionnaire nommé `bibliotheque` créé à l'étape 2), en utilisant des structures de contrôle appropriées. Chacune des entrées devrait comprendre la cote de rangement avec le titre du livre, l'auteur et la date de publication. 

Attention : Ne pas ajouter les livres qui sont déjà présents dans la collection (c'est-à-dire, les livres qui sont déjà présents dans `collection_bibliotheque.csv`) ! Utilisez des structures conditionnelles appropriées pour éviter l'ajout de ces livres en double dans le système de gestion, en se basant sur leur cote de rangement. Pour chaque livre de la nouvelle collection, affichez l'un des messages suivants selon la situation :

  - Si la cote de rangement n'est pas déjà dans la collection :
      ```
      "Le livre {cote_rangement} ---- {titre} par {auteur} ---- a été ajouté avec succès"
      ```

  - Si la cote de rangement est déjà dans la collection :
      ```
      "Le livre {cote_rangement} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque"
      ```

### Partie 3 : Modification de la cote de rangement d'une sélection de livres (3 points)
La bibliothèque souhaite faire des rénovations, et aimerait déplacer sa collection de Shakespeare dans une nouvelle rangée identifiée par "WS". Par conséquent, pour tous les livres de l'auteur William Shakespeare, la cote de rangement, qui débute actuellement par "S" suivi de 3 chiffres, devra être modifiée dans le système de gestion par "WS", suivi des mêmes trois chiffres qu'auparavant. (Par exemple, le livre ayant la cote "S028" devra être changé à "WS028"). 

Effectuez ce changement dans le système de gestion. Par la suite, affichez le système de gestion modifié afin de vérifier que le changement a été correctement effectué en utilisant `print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')`. 

### Partie 4 : Emprunts et retours de livres (5 points)
La bibliothèque souhaite tenir compte des emprunts et des retours de livres dans son système de gestion. Les cotes des livres empruntés ont été enregistrés avec la date d'emprunt dans le fichier `emprunts.csv`. 

Dans le système de gestion, commencez par ajouter une clé intitulée `emprunts` dans le dictionnaire `bibliotheque` pour suivre l'état de chaque livre. Associez à cette clé la valeur `disponible` si le livre est présent dans la bibliothèque, ou `emprunté` si le livre a été emprunté. Cette clé permettra de gérer facilement les emprunts et les retours des livres.

Par la suite, ajoutez une clé `date_emprunt`, qui contient les dates auxquelles les livres ont été empruntés. Affichez la bibliothèque mise à jour avec : `print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')`

### Partie 5 : Livres en retard (7 points)
La politique de prêt de la bibliothèque stipule que les livres doivent être retournés dans un délai de 30 jours. Si un livre n'est pas retourné dans ce délai, un frais de retard de 2$ par jour est appliqué, jusqu'à un montant maximal de 100$. Ajoutez une clé `frais_retard` et affichez la liste des livres en retard avec leurs frais respectifs en utilisant `print`.

De plus, si un livre n'a pas été retourné au bout d'un an, la bibliothèque considère le livre comme étant perdu. Identifiez les livres considérés comme perdus en ajoutant une clé `livres_perdus`, puis affichez la liste des livres perdus en utilisant : `print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')`

Indice : Pour cet exercice, vous pouvez utiliser le module [datetime](https://docs.python.org/3/library/datetime.html) intégré dans Python pour vous aider à manipuler les dates. 

## Remise du laboratoire
- Pour remettre votre travail, créez un fichier zip nommé LXX-YY-TP2.zip, où XX est le numéro de votre section de laboratoire et YY le numéro de votre équipe (par exemple, L02-04-TP2.zip pour la section 02, équipe 04).
- Ce fichier zip devra contenir uniquement votre script TP2.py. Assurez-vous d'avoir écrit votre groupe de laboratoire, numéro d'équipe, vos noms et vos matricules dans l'espace indiqué à l'intérieur du script TP2.py. 
- Avant de remettre votre travail, assurez-vous que votre script fonctionne sans erreurs, et affiche correctement tous les `print`. 
- Pour soumettre votre travail, ajoutez votre fichier zip dans la 'Boîte de remise TP2' sur Moodle. 

## Barème de correction
|     Partie    |                 Tâche                 |     Points    |
| ------------- | ------------------------------------- | ------------- |
|       1       | Créer le dictionnaire `bibliotheque`  |       2       |
|       2       | Ajout d'une nouvelle collection       |       3       |
|       3       | Modification de la cote de rangement  |       3       |
|       4       | Gestion de la clé `emprunts`          |       3       |
|       4       | Gestion de la clé `date_emprunts`     |       2       |
|       5       | Liste des livres en retard            |       4       |
|       5       | Identification des livres perdus      |       3       |
|               |                                Total  |       20      |


## Références
Les données contenues à l'intérieur des fichiers `collection_bibliotheque.csv` et `nouvelle_collection.csv` ont été tirées et adaptées de cette [base de données](https://github.com/zygmuntz/goodbooks-10k/tree/master). 
