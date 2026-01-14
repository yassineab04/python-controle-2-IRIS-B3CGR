# Devoir maison<!-- omit in toc -->

## Sommaire<!-- omit in toc -->

- [Pré-requis](#pré-requis)
- [Objectif](#objectif)
- [Comment rendre le projet](#comment-rendre-le-projet)
- [Fonctionnalités](#fonctionnalités)
  - [Menu principal /2](#menu-principal-2)
  - [Nouvelle partie /8](#nouvelle-partie-8)
  - [Historique des parties /5](#historique-des-parties-5)
  - [Statistiques /5](#statistiques-5)

## Pré-requis

Vous devez avoir Python3 d'installé sur votre machine. Vous devez savoir écrire des algorithmes en Python (variables, conditions, boucles), comment intéragir avec l'utilisateur dans le terminal et comment écrire et lire des fichiers.

Vous devez également avoir un compte Github pour pouvoir rendre le projet.

## Objectif

Développez un jeu de shifumi accessible depuis le terminal.

## Comment rendre le projet

- faire un fork de ce projet sur votre compte
- une fois votre travail terminé, faire une pull request de votre repository vers celui-ci
  - préciser dans la description ou le titre de votre pull request votre nom et votre prénom

## Fonctionnalités

### Menu principal /2

- lorsque le jeu est lancé depuis le terminal, afficher un menu permettant à l'utilisateur de choisir entre
  - commencer une nouvelle partie
  - consulter l'historique des parties précédentes
  - consulter les statistiques des parties précédentes
- laisser la possibilité à l'utilisateur de quitter le jeu

### Nouvelle partie /8

- laisser la possibilité aux joueur d'annuler la partie et de retourner au menu principal
- laisser l'utilisateur choisir entre "pierre", "feuille" et "ciseau"
- une fois le choix fait, faire jouer le CPU
- afficher le résultat de la partie
- une fois la partie terminée, laisser la possibilité à l'utilisateur
  - de retourner dans le menu principal
  - de lancer une nouvelle partie

### Historique des parties /5

- écran affichant les résultats des parties précédentes sous forme d'un tableau
  - colonne `date de la partie`
  - colonne `choix joueur`
  - colonne `choix cpu`
  - colonne `choix résultat`
- BONUS : afficher l'historique sur plusieurs pages
- laisser la possibilité à l'utilisateur de retourner dans le menu principal

### Statistiques /5

- écran affichant les statistiques des parties précédentes sous forme de liste
  - nombre de parties jouées
  - taux de victoire
  - quelle est la main la plus gagnante
    - détail des taux de victoire par main
  - BONUS : temps passé à jouer
- laisser la possibilité à l'utilisateur de retourner dans le menu principal
