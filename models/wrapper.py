class TextGenerationModel:
    def __init__(self, data_path):
        """Initializes the model, loads data from disk to RAM for
        quick access when training

        Args:
            data_path (str): path to data to load into memory
        """

        # TODO : initialize data to hold contents of files at data path

        """
            TODO : Come up with a way to store the data in memory, so that it is
            easy to work with when training our model. Maybe a dictionary of some
            sort of "song" object. Object could also store song metadata.
        """

        self.data = None