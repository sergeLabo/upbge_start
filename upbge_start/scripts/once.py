
"""
Ce script est appelé dans blender une seule fois pour initier lss variables
qui seront toutes des attributs du bge.logic (gl)
Seuls les attributs de logic sont stockés en permanence.
"""


from bge import logic as gl
from bge import events

from scripts.my_config import MyConfig
from scripts.blender_utils import get_all_objects
from scripts.blender_keyboard import Keyboard
from scripts.oscpy.server import OSCThreadServer


class MyKeyboard:
    """Key Status

    The status of a key is what informs you whether the key has just been
    pressed or if it was pressed already. The Keyboard sensor is always
    positive as long as any key is held, and you may need to trigger
    different functions when some keys are pressed and released. The status
    values are actually stored in bge.logic:

    0 = bge.logic.KX_INPUT_NONE
    1 = bge.logic.KX_INPUT_JUST_ACTIVATED
    2 = bge.logic.KX_INPUT_ACTIVE
    3 = bge.logic.KX_INPUT_JUST_RELEASED
    """

    def __init__(self):
        """Test avec la touche A"""
        self.A = 0
        self.Z = 0
        self.ECHAP = 0

    def update(self):
        a = gl.keyboard.events[events.AKEY]
        if a != 0:
            if a == 1:
                self.A = 1
            elif a == 3:
                self.A = 0

        z = gl.keyboard.events[events.ZKEY]
        if z != 0:
            if z == 1:
                self.Z = 1
            elif z == 3:
                self.Z = 0

        echap = gl.keyboard.events[events.ESCKEY]
        if echap != 0:
            if echap == 1:
                self.ECHAP = 1
            elif echap == 3:
                self.ECHAP = 0


def get_objects():
    """Retourne un dict {nom de l'objet: blender
    object}gl.all_objects[""]
    """

    gl.all_objects = get_all_objects()

    gl.cube = gl.all_objects["Cube"]
    gl.cam = gl.all_objects["Camera"]


def get_conf():
    """Récupère la configuration depuis le fichier *.ini."""

    # Le dossier courrant est le dossier dans lequel est le *.blend
    current_dir = gl.expandPath("//")
    print("Dossier courant depuis once.py {}".format(current_dir))
    gl.once = 0

    # TODO: trouver le *.ini en auto
    gl.ma_conf = MyConfig(current_dir + "scripts/upbge.ini")
    gl.conf = gl.ma_conf.conf

    print("\nConfiguration du jeu upbge:")
    print(gl.conf, "\n")


def set_variables():
    # Suivi des frames
    gl.frame = 0


def create_server():
    ip = gl.conf['osc']['ip']
    port = int(gl.conf['osc']['port'])
    gl.osc = OSCThreadServer()
    gl.socket_server = gl.osc.listen(   address=ip,
                                        port=port,
                                        default=True)

    @gl.osc.address(b'/action')
    def callback(*values):
        # # print(f"actions: {values}")
        gl.actions = values


    @gl.osc.address(b'/depth')
    def callback(*values):
        print(f"depth: {values}")
        gl.depth = values


def main():
    """Lancé une seule fois à la 1ère frame au début du jeu par main_once."""

    print("Initialisation des scripts lancée un seule fois au début du jeu.")

    # Récupération de la configuration
    get_conf()

    # Initialisation de toutes les variables
    set_variables()

    # Initialisation du serveur
    if gl.conf['osc']['server']:
        create_server()

    # Récupération des objets Blender
    get_objects()

    # Capture clavier
    gl.kbd = MyKeyboard()

    # Pour les mondoshawan
    print("ok once.py")
