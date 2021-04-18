import os
import shutil
from pathlib import Path


def main():
    """Clear the data directory of all downloaded data
    """

    folder = str(Path().resolve().parent) + "/data/"

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    print('Deleted Data')


if __name__ == "__main__":
    main()
