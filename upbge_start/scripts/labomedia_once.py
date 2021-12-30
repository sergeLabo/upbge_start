
"""
Ne jamais modifier ce script.

Les scripts:
- labomedia_once.py
- labomedia_always.py
sont les seuls scripts importés directement dans Blender.
Ils sont importés en tant que module, et ne sont compilé qu'une seule fois.

Les autres scripts sont aussi importés en temps que modules.
Il est possible de les modifier dans un éditeur externe
sans avoir à les recharger dans Blender,
il suffit de les enregistrer avant de lancer le jeu.
"""

# imports locaux
from scripts import once


def main():
    """Fonction lancée à la 1ère frame dans blender."""

    once.main()
