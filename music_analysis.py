import csv
import pylast
import time


def parse_pylast_top_tags(top_tags):
    tags = []
    for tag in top_tags:
        tags.append(tag.item.name.lower())
    return tags

API_KEY = "4d9b3cb29dbdb6d8b3c760c507c0ceb0"
API_SECRET = "d71a1d2bb2354bd1d6af3d6d129779da"

username="kcingel"
password_hash = pylast.md5("Don'tStealMyPwd1995!")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)
music_library_filename="/Users/kcingel/PycharmProjects/my_music_library_analysis/KaseysMusicLibrary.csv"


master_music_library_filename="/Users/kcingel/PycharmProjects/my_music_library_analysis/MasterMusicLibrary.csv"
master_music_library_file = open(master_music_library_filename,"w")

track=network.get_track("Iron Maiden","The Nomad")
pylast_tags = track.get_top_tags(limit=None)
tags = parse_pylast_top_tags(pylast_tags)
print(tags)
artist="Neon Trees"
name="Animal"
track=network.get_track(artist,name)
track.get_top_tags(limit=None)
all_songs = {}
with open(music_library_filename,'r',encoding='iso-8859-1') as music_library_csv:
    csv_reader = csv.reader(music_library_csv,delimiter=',')
    for row in csv_reader:
        song_name = row[0].strip()
        all_songs[song_name]={}
        artist=row[1].strip()
        all_songs[song_name]['artist']=artist
        album=row[2]
        all_songs[song_name]['album']=row[2]
        added_date=row[3]
        all_songs[song_name]['added date']=added_date
        try:
            track = network.get_track(artist, song_name)
            print(track)
            time.sleep(2)
            pylast_tags = track.get_top_tags(limit=None)
            tags = parse_pylast_top_tags(pylast_tags)
            print(tags)
        except:
            print("Track " + song_name + " not found")
            continue;


























