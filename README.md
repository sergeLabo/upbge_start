# UPBGE Game Base

Les bases pour commencer un jeu dans UPBGE 0.30, sous Debian 11 Bullseye, python3.9

### Philosophie
Ce jeu sert de base pour la création d'un univers avec une interaction en temps réel. Je suis en concurrence directe avec un certain Mark de chez Fac.... et Bai... Trop fort.

### Installation
#### Installation de UPBGE
Récupération du ZIP à https://upbge.org/#/download

Décomprésser dans un dossier réservé aux sources de Blender

### Création de liens pour lancer facilement UPBGE
Dans ce dossier, ouvrir un terminal:
``` bash
sudo ln -s blenderplayer /usr/bin/blenderplayer
sudo mv /usr/bin/blender /usr/bin/blender3D
sudo ln -s blender /usr/bin/blender
```

Du  coup, pour lancer le Blender Original:
``` bash
blender3D
```
UPBGE se lance avec:
``` bash
blender
blenderplayer
```

### Principe de mes scripts

Sur le Cube au centre de la scène, il y a quelques briques qui excécute:

* labomedia_once.py une seule fois. Ce script appelle once.py qui initie toutes les objets python et leurs attributs, et toutes les  variables
* labomedia_always.py ensuite à chaque frame. Ce script appelle always.py en tant que module(il n'est donc compiler qu'une seule fois). Ce script va tout faire, il n'y aura pas d'autres briques logiques.
* Il ne faut jamais modifier labomedia_once.py et labomedia_always.py. Les autres scripts n'ont pas à être recharger dans Blender, il suffit d'utiliser un bon EDI et d'enregister tous les fichiers dans l'EDI.
* Mettre le Cube en Invisible et Ghost

#### Explications
Des scripts "outils" permettent de:

* récupérer tous les objets: Exemple le Cube est gl.cube = gl.all_objects["Cube"]
* Agir facilement sur tous les objets, position, rotation, scale
* Ajouter, cacher des objets ...

C'est beaucoup plus facile de le faire en python en structurant, en appelant d'autres scripts ...

### Lancement du jeu
run_upbge_start.sh doit être excécutable. Dans le dossier:
``` bash
./run_upbge_start.sh
```
Vous pouvez créer un lanceur sur votre bureau

### Configuration
Il faut modifier le fichier upbge.ini

#### Serveur OSC pour recevoir et envoyer

Configurer [osc] et modifier create_server() dans once.py




