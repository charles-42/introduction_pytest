# Introduction_pytest

## Pourquoi automatiser ses tests

Quand on code une fonction, c'est quelque chose de très naturel de la tester. Du moins de réaliser des tests manuels sur ce qu'on vient de coder.
On peut prendre l'exemple de la fonction suivante codée dans [basics/src/inverse](basics/src/inverse.py):

**`Créer une fonction inverse() qui:`**
- pour une chaine de caractère en minuscule: renvoie la chaîne de caractère inverse en minuscule
- pour un integer : renvoie une erreur
- pour une liste:
  - si elle n'est que composée de strings: concatène et renvoie l'inverse
  - sinon renvoie une erreur.
  - par contre si la liste possède 4 éléments , enlève dernier avant d'inverser

Tester une fonctionnalité juste après l'avoir codée, c'est le principe du `test unitaire`. Ce qui est moins naturel, mais surtout qui devient très chronophage quand on a un code important, c’est tester manuellement que ce qu’on vient de coder n’a rien cassé.
C’est pour cela qu’il est primordial d’automatiser ses tests.


## Qu’est ce qu’un test

On peut voir des premiers tests dans [basics/tests/first_test.py](basics/tests/first_test.py).
Un test c’est:
- Une fonction
- qui respecte une convention de nommage, dans un fichier qui respecte une convention de nommage
- qui met en place un contexte de test, ce qui correspond souvent à l’appel de la fonction à tester
- et qui réaliser un ensemble d’assertion

Les assertions correspondent à ce qu’on attend de la fonction à tester. On ne tests toujours certains cas de figure, c'est -à -dire qu’on appelle la fonction avec certains paramètres et on valide que la fonction renvoie ce que l’on attend ou qu’elle agit comme on l’attend.

La convention de nommage est primordiale pour que pytest puisse “collecter” nos tests. Elle est la suivante:
- aucune règles sur les dossiers: pytest parcours tous les dossiers à partir de la racine
- les fichiers doivent commencer par “test_”  ou finir par “_test.py”
- les fonctions doivent commencer par test_

## Lancer les tests

Pour lancer les tests il suffit d’exécuter “pytest” (dans l’environnement virtuel dans lequel pytest est installé

Il y a plusieurs commandes spécifiques à connaître:

```bash
pytest folder_name # ne tester qu’un seul dossier
pytest folder_nam/file_name::function_name # ne tester qu’une seule fonction
pytest -s # afficher les prints qu’ont a écrit dans nos tests
pytest -v # avoir plus de détails sur nos tests
```

## Que faut il tester

Savoir ce qu’il faut tester est toujours compliqué. La règle général est de tester que ce dont est responsable la fonction. C’est le principe du test unitaire. 

On veut coder la fonctionnalité suivante:
- A partir du nom d’un apprenant, on veut retrouver ses notes dans une base de données 
- On veut ensuite éditer un fichier au format pdf avec le bulletin de l'apprenant. 

La bonne pratique est de séparer les responsabilités. Il faut développer:
- Une fonction ‘get_grades” qui va chercher les notes en bases de donnés (fonction qui existe déjà dans de nombreux packages comme sqlalchemy ou pandas)
- Une fonction ‘record_edition” qui crée le bulletin à partir des notes.

Quand on réalise le test unitaire de la fonction record_edition il ne faut tester que sa responsabilité, savoir donc si à partir de notes on arrive à créer un pdf. Le fait d’être capable d’aller chercher avec succès les notes d’un apprenant à partir de son nom est de la responsabilité de la fonction  "get_grades”. 

Si on veut tester tous les process, ce n’est plus un test unitaire mais un test d’intégration.

Une fois qu’on a identifié la responsabilité de la fonction qu’on code/ qu’on teste, se pose la questions des scénarios qu’il faut tester. L’idée est de tester l’ensemble des scénarios critiques. Cela veut donc dire:
- ne pas faire trop d’assertion redondante
- réussir à se repérer qu’elles sont les cas critiques. Par exemple la division par 0 quand on fait un multiplication

C’est difficile de penser à tous les cas critiques:
- certains sont évidents par la manière dont la fonction est codée, par exemple quand elle prévoit de base certaines exceptions dans son fonctionnement, il faut tester que ces exceptions sont bien levées
- l’expérience aide aussi à trouver ces cas critiques, on sait par exemple que dans une base de données on peut faire une requete qui ne renvoie pas d’erreur mais qui n’a trouvé aucun résultat
- enfin la pratique sert aussi, si certains cas critiques ne sont pas identifiées au moment du développement, ils amèneront des erreurs dont ou pourra se servir pour ajouter des tests

On peut voir l’exemple des ces fichiers de [fonctions à tester](exercices/src/fonctions_simples.py) et des [tests correspondants](exercices/tests/test_fonctions_simples.py)


## Quelques techniques de test avancées

Si beaucoup de tests consistent à affirmer que le retour de la fonction à telle ou telle valeur, certaines fonctions sont un peu plus difficiles à tester. On peut retrouver trois exemples de [fonctions](exercices/src/fonctions_difficiles.py)  et leurs [tests](exercices/tests/test_fonctions_difficiles.py) correspondant dans ce repo.

On a identifié trois cas:

Le premier, qui rappelle le rapport entre get_grades et record_edition, c’est quand une fonction dépend d’une autre fonction dont on maîtrise mal le résultat (appel à une api, requête de BDD, input de l’utilisateur). Pour tester unitairement cette fonction, la bonne pratique est de simuler le fonctionnement de la fonction dont elle dépend pour qu’elle revoie toujours la même valeur


Le deuxième est un exemple de cas où nos fonctions agissent sur des fichiers ou des BDD qu’on ne veut pas modifier à cause de nos tests. La bonne pratique consiste ici à créer des fichiers ou des BDD de tests qui n’existeront que le temps du test et seront automatiquement supprimés ensuite.


Le troisième est celui où la fonction à tester à un comportement aléatoire; Il faut alors fixer la seed de cet aléa pour supprimer l’effet aléatoire. 

## Quand tester nos fonctions

Assez naturellement on teste nos fonctions juste après les avoir développées. Cependant quand on travaille à plusieurs sur notre projet, il est important de pouvoir partager à nos collaborateurs les résultats de nos tests avant d’intégrer notre code au projet. Ainsi une bonne pratique consiste à créer un pipeline de continuous intégration qui déclenchera l'exécution de nos tests dès qu’on push notre code sur github ou qu’on réalise une pull request.

Il faut noter que si nos tests échouent, notre code est tout de même pushé en ligne. C’est pour cela qu’il est important de travailler sur des branches et d’ajouter notre code au main qu’au seul moyen des pulls requests.

[exemple de pipeline CI](.github/workflows/ci.yaml)

## La couverture de test

Le package coverage permet de savoir si notre code est bien couvert par des tests.
Il évalue quelle proportion de notre code se trouve dans des fonctions testées. Ainsi tout code qui n’est pas dans une fonction ou n’est pas dans une fonction testée, fera baisser la couverture.

La couverture est un outil mais il faut connaître ses limites:
- il y a du code qu’on ne peut pas mettre dans des fonctions
- une fonction testées n’est pas nécessairement une fonction bien testée

Pour évaluer sa couverture:

```bash
pytest --cov
pytest --cov --cov-fail-under=95
```

Pour en savoir plus [cours openclassroom](https://openclassrooms.com/fr/courses/7747411-test-your-python-project/7895249-measure-your-code-coverage)

## Conclusion

Avoir un code testé possède de nombreux avantages:
- S’assurer qu’on ne casse rien quand on crée une nouvelle fonctionnalité
- Etre au clair sur ce qu’on attend des fonctions qu’on code
- Se forcer se projeter dans les cas critiques d’usage de nos fonctionnalités
- Ecrire du code propre car le code propre est plus facilement testable 
