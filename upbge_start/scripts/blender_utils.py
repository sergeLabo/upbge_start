

import inspect

from bge import logic as gl



def get_all_objects():
    """
    Trouve tous les objets des scènes actives
    Retourne un dict {nom de l'objet: blender object}
    """

    activeScenes, scene_name = get_all_scenes()

    all_obj = {}
    for scn_name in scene_name:
        scn = get_scene_with_name(scn_name)
        for blender_obj in scn.objects:
            blender_objet_name = blender_obj.name
            all_obj[blender_objet_name] = blender_obj

    return all_obj

def get_all_scenes():
    """Récupération des scènes"""

    # Liste des objets scènes
    activeScenes = gl.getSceneList()

    # Liste des noms de scènes
    scene_name = []
    for scn in activeScenes:
        scene_name.append(scn.name)

    return activeScenes, scene_name

def get_scene_with_name(scn):
    """Récupération de la scène avec le nom"""

    activeScenes, scene_name = get_all_scenes()
    if scn in scene_name:
        return activeScenes[scene_name.index(scn)]
    else:
        print(scn, "pas dans la liste")
        return None

def add_object(obj, position, life, all_obj, game_scn):
    """
    Ajoute obj à la place de Empty
    position liste de 3

    addObject(object, reference, time=0)
    Adds an object to the scene like the Add Object Actuator would.
    Parameters:
        object (KX_GameObject or string) – The (name of the) object to add.
        reference (KX_GameObject or string) – The (name of the) object which
        position, orientation, and scale to copy (optional), if the object
        to add is a light and there is not reference the light’s layer will be
        the same that the active layer in the blender scene.
        time (integer) – The lifetime of the added object, in frames. A time
        of 0 means the object will last forever (optional).

    Returns: The newly added object.
    Return type: KX_GameObject
    """
    empty = all_obj['Empty']
    empty.worldPosition = position

    return game_scn.addObject(obj, empty, life)

def droiteAffine(x1, y1, x2, y2):
    """
    Retourne les valeurs de a et b de y=ax+b
    à partir des coordonnées de 2 points.
    """

    a = (y2 - y1) / (x2 - x1)
    b = y1 - (a * x1)
    return a, b

def scene_change(sceneOld, sceneNew):
    """
    End of sceneOld, load sceneNew.
    Scene must be str: if scene = scene python object, name is scene.name
    """
    scenes = gl.getSceneList()
    print("Scenes list in scene_change() =", scenes)
    # Check name
    scnName = []
    for scn in scenes:
        scnName.append(scn.name)
    if not sceneOld in scnName:
        print("  {} isn't in scenes list".format(sceneOld))
    else:
        gl.tempoDict["scene_change"].unlock()
        gl.tempoDict["scene_change"].reset()
        print("  Tempo scene_change reset and unlock")

        for scn in scenes:
            if scn.name == sceneOld:
                scn.end()
                print("  End of scene: {}".format(scn))
        try:
            gl.addScene(sceneNew)
            print("  Scene {0} added".format(sceneNew))
        except:
            print("  Scene {0} doesn't exist: Can't be set.".format(sceneNew))

def print_str_args(*args):
    """
    Imprime en terminal les variables en argument
    Les variables doivent être sous forme de string,
    par exemple
    print_str_args("a")
    imprime la variable a qui a une valeur 42
    a = 42
    """

    for i in args:
        record=inspect.getouterframes(inspect.currentframe())[1]
        frame=record[0]
        val=eval(i,frame.f_globals,frame.f_locals)
        print('{0} = {1}'.format(i, val))
