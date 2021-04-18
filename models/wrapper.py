from pathlib import Path
import ast


class TextGenerationModel:
    songs = {}

    def __init__(self, file_name):
        """Initializes the model, loads data from disk to RAM for
        quick access when training

        Args:
            file_name (str): name of txt file with song lyrics
        """

        data_folder_path = str(Path().resolve().parent) + "/data/"

        dict_strings_files = open(data_folder_path + file_name, "r")
        self.songs = ast.literal_eval(dict_strings_files.read())
        dict_strings_files.close()
