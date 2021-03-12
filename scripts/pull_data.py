# Imports
import json
import argparse
from pathlib import Path

# Constants
DATA_DIR = Path('../data/')
SECRETS = Path('./secrets.json')

"""
    This script downloads song data corresponding to the passed parameters

        Example usage (in scripts directory):
            python pull_data.py --genre "Hip Hop"
"""

def download_genre(genre):
    """Download the data for a given genre, and save to the project's
    data directory

    Args:
        genre (str): genre to pull song data for
    """

    # TODO : Download the data

    # TODO : Validate data integrity (if necessary)

    # TODO : Reformat data prior to save (if necessary)

    pass

def download_artist(artist):
    """Download the data for a given artist, and save to the project's
    data directory

    Args:
        artist (str): artist to pull song data for
    """

    # TODO : Download the data

    # TODO : Validate data integrity (if necessary)

    # TODO : Reformat data prior to save (if necessary)

    pass

def main(args):
    """Validates the arguments passed, launches data download

    Args:
        args (object): command line arguments passed to the script
    """

    # TODO : Make sure that one of genre or artist was passed as an argument

    # TODO : Make sure that the genre/artist passed is valid

    # TODO : Launch download of data

    with open(SECRETS) as secrets_f:
        secrets = json.load(secrets_f)
        print('Key: {}\n'.format(secrets['keys']['genius']))

    print('*****Passed Arguments*****\nGenre: {}\nArtist: {}'.format(args.genre, args.artist))
    print('This is the data directory: {}'.format(DATA_DIR))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Songster data ')

    parser.add_argument('--genre', dest='genre', type=str, default=None,
                        help='download music from the passed genre')
    parser.add_argument('--artist', dest='artist', type=str, default=None,
                        help='download music from the passed artist')
                        
    args = parser.parse_args()
    main(args)