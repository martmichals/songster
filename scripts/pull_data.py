# Imports
import lyricsgenius
import json
import argparse
from pathlib import Path

# Constants
DATA_DIR = Path('../data/')

with open('secrets.json') as f:
    secret_file = json.load(f)
genius = lyricsgenius.Genius(secret_file["keys"]["genius"])

"""
    This script downloads song data corresponding to the passed parameters

        Example usage (in scripts directory):
            python pull_data.py --genre "Hip Hop"
"""


def download_genre(genre, page_limit=2):
    """Download the data for a given genre, and save to the project's
    data directory

    Args:
        genre (str): genre to pull song data for
        page_limit (int): limits number of pages to be scraped
    """

    page = 1
    all_lyrics = {}
    while page < page_limit and page:
        response = genius.tag(genre, page=page)
        for hit in response['hits']:
            lyrics = genius.lyrics(song_url=hit['url'])
            all_lyrics[hit['title']] = clean_lyrics(lyrics)
        page = response['next_page']

    write_dict_to_file(genre, all_lyrics)

    return all_lyrics


def download_artist(artist, page_limit=2, page_size=5):
    """Download the data for a given artist, and save to the project's
    data directory

    Args:
        artist (str): artist to pull song data for
        page_limit (int): limits number of pages to be scraped
        page_size (int): limits how many songs per page
    Returns:
        (str): name of artist
        (dict): dictionary containing song titles and lyrics
    """

    genius_artist = genius.search_artist(artist, max_songs=1)
    page = 1
    songs = []
    all_lyrics = {}

    while page < page_limit and page:
        request = genius.artist_songs(genius_artist.id,
                                      sort='popularity',
                                      per_page=page_size,
                                      page=page)
        songs.extend(request['songs'])

        for song in request['songs']:
            title = song['title']
            lyrics = genius.search_song(title, genius_artist.name).lyrics
            all_lyrics[title] = clean_lyrics(lyrics)

        page = request['next_page']

    write_dict_to_file(genius_artist.name, all_lyrics)

    return genius_artist.name, all_lyrics


def clean_lyrics(lyrics):
    """ Removes bracketed sections (eg. [Chorus 1: John]) and removes line breaks

    Args:
        lyrics (str): lyrics to be cleaned
    Returns:
        (str): clean lyrics
    """
    lyrics.replace("\n", " ").replace("\r", " ")

    lyrics_index = 0
    while lyrics_index < len(lyrics):
        if lyrics[lyrics_index] == '[':
            sub_index = lyrics_index
            while lyrics[sub_index] != ']':
                sub_index += 1
            lyrics = lyrics[: lyrics_index] + lyrics[sub_index + 1:]

        lyrics_index += 1

    return lyrics


def write_dict_to_file(artist_name, lyric_dict):
    formatted_artist_name = ""
    for item in artist_name.split(" "):
        formatted_artist_name += item + "_"

    file_path = formatted_artist_name + "lyrics.txt"
    data = str(lyric_dict)

    file_writer = open(file_path, 'wt')
    file_writer.write(data)


def main(args):
    """Validates the arguments passed, launches data download

    Args:
        args (object): command line arguments passed to the script
    """

    # TODO : Make sure that one of genre or artist was passed as an argument

    # TODO : Make sure that the genre/artist passed is valid

    # TODO : Launch download of data

    print('*****Passed Arguments*****\nGenre: {}\nArtist: {}'.format(args.genre, args.artist))
    print('This is the data directory: {}'.format(DATA_DIR))

    if args.artist is not None:
        download_artist(args.artist)
    if args.genre is not None:
        download_genre(args.genre)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Songster data ')

    parser.add_argument('--genre', dest='genre', type=str, default=None,
                        help='download music from the passed genre')
    parser.add_argument('--artist', dest='artist', type=str, default=None,
                        help='download music from the passed artist')
                        
    args = parser.parse_args()
    main(args)
