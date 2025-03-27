# Enigma

# Projet : Simulation de la Machine Enigma en Python

## Description

Ce projet est une simulation de la machine Enigma, un système de chiffrement symétrique utilisé pendant la Seconde Guerre mondiale. Il permet de chiffrer et déchiffrer un texte en utilisant une configuration de rotors définie par l'utilisateur. L'interface utilisateur est en ligne de commande.

---

## Prérequis

Avant d'exécuter ce projet, voici les éléments qui devraient être installés :

### 1. Versions requises

- **Python** : 3.8 ou supérieur
- **Systèmes d'exploitation** : macOS (M1/M2 compatible), Windows, Linux

### 2. Bibliothèques Python nécessaires

Installez les dépendances en exécutant la commande suivante :

#### Sur Linux / macOS :

```sh
pip3 install art colorama rich
```

#### Sur Windows :

```sh
pip install art colorama rich
```

### 3. Vérification de l'installation

Vous pouvez vérifier que Python est installé avec la commande :

#### Sur Linux / macOS :

```sh
python3 --version
```

#### Sur Windows :

```sh
python --version
```

---

## Installation et Exécution

### 1. Cloner le dépôt

Si ce projet est stocké sur un dépôt Git, clonez-le avec :

#### Sur Linux / macOS :

```sh
git clone https://github.com/tdu7/Enigma.git
cd <nom_de_votre_dossier>
```

#### Sur Windows :

```sh
git clone https://github.com/tdu7/Enigma.git
cd <nom_de_votre_dossier>
```

### 2. Exécuter le programme

#### Sur Linux / macOS :

```sh
python3 enigma.py
```

#### Sur Windows :

```sh
python enigma.py
```

---

## Fonctionnalités

- **Affichage stylisé** du texte d'accueil et des options avec des couleurs.
- **Chiffrement et déchiffrement** d'une chaîne de caractères avec une configuration de rotors.
- **Interaction utilisateur** avec des choix clairs pour chiffrer ou déchiffrer un message.
- **Gestion des erreurs des entrées.**

---

## Utilisation

1. Au lancement, un message de bienvenue s'affiche et toutes les instructions sont directement affichées en ligne de commande.

   L'utilisateur doit définir la configuration des rotors avec 3 lettres de l'alphabets  (ex : `abc`).

   Ensuite, il peut choisir :
   - `C` pour chiffrer un message.
   - `D` pour déchiffrer un message.
     Le programme retourne le texte transformé et propose d'inverser l'opération.
     Pour quitter la boucle de l'exécution du script, l'utilisateur peut entrer la lettre`q`.

---

## Auteurs

**Annaelle Tomkeu Dassy** - Développeuse&#x20;




