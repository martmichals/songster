# Imports
import lyricsgenius
import json
import argparse
from pathlib import Path
import os
import re

# Constants
DATA_DIR = Path('../data/')
SECRETS = Path('./secrets.json')

"""
    This script downloads song data corresponding to the passed parameters

        Example usage (in scripts directory):
            python pull_data.py --genre "Hip Hop"
"""


def download_genre(genius, genre, song_count_limit):
    """Download the data for a given genre, and save to the project's
    data directory

    Args:
        genre (str): genre to pull song data for
        song_count_limit (int): limits # of songs being pulled
    """

    page = 1
    all_lyrics = {}
    while len(all_lyrics) < song_count_limit and page:
        response = genius.tag(genre, page=page)
        for hit in response['hits']:
            lyrics = genius.lyrics(song_url=hit['url'])
            all_lyrics[hit['title']] = clean_lyrics(lyrics)
        page = response['next_page']

    write_dict_to_file(genre, all_lyrics)

    return all_lyrics


def download_artist(genius, artist, song_count_limit):
    """Download the data for a given artist, and save to the project's
    data directory

    Args:
        genius (obj): genius API object
        artist (str): artist to pull song data for
        song_count_limit (int): limits # of songs being pulled
    Returns:
        (str): name of artist
        (dict): dictionary containing song titles and lyrics
    """

    genius_artist = genius.search_artist(artist, max_songs=song_count_limit, include_features=True)
    all_lyrics = {}

    for song in genius_artist.songs:
        title = song.title
        try:
            lyrics = song.lyrics
        except AttributeError:
            continue
        all_lyrics[title] = clean_lyrics(lyrics)

    write_dict_to_file(genius_artist.name, all_lyrics)

    return genius_artist.name, all_lyrics


def clean_lyrics(lyrics):
    """ Removes bracketed sections (eg. [Chorus 1: John]) and removes line breaks

    Args:
        lyrics (str): lyrics to be cleaned
    Returns:
        (str): cleaned up lyrics
    """
    # Strip all unicode
    # lyrics = lyrics.encode('ascii', 'ignore').decode()
    lyrics = ''.join([i if ord(i) < 128 else ' ' for i in lyrics])
    lyrics = lyrics.replace(",", "")
    lyrics = lyrics.replace("'", "")
    lyrics = lyrics.replace(" . ", "")
    lyrics = lyrics.replace(";", "")
    lyrics = lyrics.replace("''", "")

    # Delete all bracketed sections
    lyrics = re.sub(r'\[[^][]*\]', '', lyrics)

    # Strip leading, trailing whitespace, add newline to the end of the string
    lyrics = 'START ' + lyrics.strip() + '\n'

    # Replace all multiple and single newline sequences with start tags
    lyrics = re.sub(r'\n+', ' END\n', lyrics)

    # Add start tags
    lyrics = re.sub(r'\n(?=.)', '\nSTART ', lyrics)

    # Delete all parentheses
    lyrics = re.sub('[()]', '', lyrics)

    # Replaces newlines with spaces
    lyrics = lyrics.replace('\n', ' ')

    return lyrics


def write_dict_to_file(artist_name, lyric_dict):
    """ Writes passed dictionary to a file in the data folder, creates data
    folder if it doesn't already exist

    Args:
        artist_name (str): name of the artist or genre
        lyric_dict (dict): dictionary with song name as keys and lyrics as value
    """

    # Strip unicode characters from keys
    lyric_dict = {key.encode('ascii', 'ignore').decode(): lyric_dict[key] for key in lyric_dict}

    file_path = str(Path().resolve().parent) + "/data/"
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    formatted_artist_name = ""
    for name in artist_name.split(" "):
        formatted_artist_name += name + "_"
    file_name = formatted_artist_name + "lyrics.txt"

    data = str(lyric_dict)
    file_writer = open(file_path + file_name, 'w+', encoding="utf-8", errors="ignore")
    file_writer.write(data)


def main(args):
    """Validates the arguments passed, launches data download
    Args:
        args (object): command line arguments passed to the script
    """

    with open(SECRETS) as secrets_f:
        secrets = json.load(secrets_f)
        genius = lyricsgenius.Genius(secrets['keys']['genius'])

    print('*****Passed Arguments*****\nGenre: {}\nArtist: '
          '{}\nLimit: {}'.format(args.genre, args.artist, args.limit))

    song_count_limit = args.limit

    if args.artist is not None:
        download_artist(genius, args.artist, song_count_limit)
    if args.genre is not None:
        download_genre(genius, args.genre, song_count_limit)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Songster data')

    parser.add_argument('--genre', dest='genre', type=str, default=None,
                        help='download music from the passed genre')
    parser.add_argument('--artist', dest='artist', type=str, default=None,
                        help='download music from the passed artist')
    parser.add_argument('--limit', dest='limit', type=int, default=20,
                        help='limits number of downloaded songs')

    args = parser.parse_args()
    main(args)
