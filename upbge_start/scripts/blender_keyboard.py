
"""
Perrmet des entrées clavier sans Logics Bricks
"""

class VirtualEvents:
    def __init__(self):
        self.UPARROWKEY = 0
        self.DOWNARROWKEY = 0
        self.SPACEKEY = 0
        self.AKEY = 0
        self.BKEY = 0

try:
    from bge import events
except:
    print("Import de events impossible")
    events = VirtualEvents()


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

SPECIALS = {    'UP':   events.UPARROWKEY,
                'DOWN': events.DOWNARROWKEY,
                'SPACE': events.SPACEKEY}



class Keyboard:
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

    def __init__(self, onces=LETTERS, held=SPECIALS):
        """Liste des touches:
            onces =  action une seule fois, même si maintenu
            held = action continue si active
        """

        self.onces = onces
        self.held = held

        # Transformation d'un string en variable locale locals()[lettre] = 0
        for lettre in self.onces:
            #setattr(someobject, foostring, value)
            setattr(self, lettre, 0)

    def update(self):
        print(dir(self))
        self.keyboard_once()
        # # self.keyboard_hold()

    def keyboard_once(self):
        for lettre in self.onces:
            if self.lettre == 0:
                setattr(self, lettre, 1)
            # # if events[lettre] == 3:
                # # setattr(self, lettre, 0)

    # # def keyboard_hold(self):
        # # for lettre in self.onces:
            # # if getattr(self, lettre, 3) and events[lettre] == 2:
                # # setattr(self, lettre, 0)




if __name__ == "__main__":
    from time import sleep
    kbd = Keyboard()
    while 1:
        print(kbd.A)
        sleep(0.1)
