
"""
Lancé à chaque frame durant tout le jeu.
"""


from bge import logic as gl

from scripts.blender_utils import get_scene_with_name, add_object, droiteAffine

def main():

    gl.frame += 1
    gl.kbd.update()
    print(gl.kbd.A, gl.kbd.Z, gl.kbd.ECHAP)

    # Quit du jeu proprement avec Echap
    if gl.kbd.ECHAP:
        gl.osc.close()
        gl.endGame()
