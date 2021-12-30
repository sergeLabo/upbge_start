
import os
import subprocess
from pathlib import Path
from json import dumps, loads


class Utils:

    def get_all_files_list(self, directory, extentions):
        """
        Lit le dossier et tous les sous-dosssiers.
        Retourne la liste de tous les fichiers avec les extentions de
        la liste extentions.
        """

        file_list = []
        for path, subdirs, files in os.walk(directory):
            for name in files:
                for extention in extentions:
                    if name.endswith(extention):
                        file_list.append(str(Path(path, name)))

        return file_list

    def get_all_sub_directories(self, root):
        """
        Retourne la liste de tous les sous-répertoires,
        et du répertoire,
        y compris les __pycache__
        """

        return [x[0] for x in os.walk(root)]

    def read_file(self, file_name):
        """
        Retourne les datas lues dans le fichier avec son chemin/nom
        Retourne None si fichier inexistant ou impossible à lire .
        """

        try:
            with open(file_name) as f:
                data = f.read()
        except:
            data = None
            print("Fichier inexistant ou impossible à lire:", file_name)

        return data

    def write_data_in_file(self, data, fichier, mode="w"):
        """
        Ecrit data dans le fichier.
        Mode 'w' écrit un string dans le fichier
        Mode 'wb' écrit des bytes dans le fichier
        w écrase
        a ajoute
        """
        with open(fichier, mode) as fd:
            fd.write(data)

    def write_data_in_file_create_dir_if_needed(self, data, fichier,
                                                base, mode="w"):
        """
        Crée les sous dossiers si besoin, fichier est le chemin absolu

        Attention: ça peut créer des dossiers n'importe où !!!!!!!!!!!!!
        TODO: faire une limitation avec un argument de chemin de base

        abs = /media/data/3D/projets/police_du_wiki/toto/file.txt
        chemin de base = /media/data/3D/projets/police_du_wiki
        on ne peut créer que dans le dossier chemin de base

        Ecrit data dans le fichier.
        Mode 'w' écrit un string dans le fichier
        Mode 'wb' écrit des bytes dans le fichier
        w écrase
        a ajoute
        """

        with open(fichier, mode) as fd:
            fd.write(data)

    def data_to_json(self, data):
        """Retourne le json des datas"""

        return dumps(data)

    def get_json_file(self, fichier):
        """
        Retourne le json décodé des datas lues
        dans le fichier avec son chemin/nom.
        """
        with open(fichier) as f:
            data = f.read()
        data = loads(data)
        return data

    def print_all_key_value(self, my_dict):
        """
        Imprime un dict contenant un dict,
        affiche le nombre de clés total.
        """

        total = 0

        for k, v in my_dict.items():
            print(k)
            for f in v:
                total += 1
                print("    ", f)
        print("Nombre de clés total =", total)
        print("pour un théorique par jour de =", 24*1)

    def create_directory(self, directory):
        """
        Crée le répertoire avec le chemin absolu, ou relatif:
        """

        try:
            # mode=0o777 est par défaut
            Path(directory).mkdir(mode=0o777, parents=False)
            print("Création du répertoire: {}".format(directory))
        except FileExistsError as e:
            print("Le répertoire {} existe.".format(directory))
        except PermissionError as e:
            print("Problème de droits avec le répertoire {}".format(directory))
        except:
            print("Erreur avec {}".format(directory))
            os._exit(0)

    def get_absolute_path(self, a_file_or_a_directory):
        """
        Retourne le chemin absolu d'un répertoire ou d'un fichier
        n'importe où.

        Valable depuis le script courrant ou en import depuis un autre script
        get_absolute_path(__file__)
        """

        return os.path.abspath(a_file_or_a_directory)

    def run_command_system(self, command):
        """
        Excécute la command shell.
        command = liste
        """
        #resp = subprocess.call(command.split())
        #resp = subprocess.getoutput(command.split()

        p = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, errors = p.communicate()

        return output.decode('utf-8')
