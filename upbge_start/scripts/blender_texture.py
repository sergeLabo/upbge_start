

"""
Class générique qui permet de changer la texture d'un objet.
Ce script ne peut tourner que dans blender.
"""



class TextureChange():
    """
    Classe générique utilisable dans d'autres projects,
    pour changer une texture d'un objet.
    """

    def __init__(self, obj, old_tex):
        """
        obj     = objet concerné
        old_tex = image de la texture originale, ex "danseur2.png"
        new_tex = "//textures/perso.png"
        """

        self.old_tex = old_tex
        # ID de la texture existante
        self.ID = texture.materialID(obj, 'IM' + old_tex)
        # Sauvegarde de l'objet python dans le Game Logic
        self.obj_texture = texture.Texture(obj, self.ID)

    def texture_new(self, new_tex):
        """
        Application de la nouvelle image de la texture.

        Répéter la fonction plusieurs fois (ex 5x) pour que
        le changement marche.
        Tous les object avec le matériau seront changés.
        """

        # Nouvelle source
        url = gl.expandPath(new_tex)
        print("Path du fichier", new_tex, "=", url)

        new_source = texture.ImageFFmpeg(url)

        # Remplacement
        self.obj_texture.source = new_source
        self.obj_texture.refresh(False)

    def texture2old(self):
        """
        Effacement de l'objet python, pour retourner à l'ancienne texture.
        """

        try:
            del self.obj_texture
        except:
            print("Problème avec la suppression de la texture:", self.obj_texture)
