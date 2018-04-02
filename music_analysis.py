import csv
import pylast
import time
from collections import Counter


def parse_pylast_top_tags(top_tags):
    tags = []
    for tag in top_tags:
        tags.append(tag.item.name.lower())
    return tags

# Method to adjust the master dictionary of all tags with how frequently the tag appears in music library based on
# the current song tags. If tag in current_song_tags is not already in all_tags_with_counts, tag is added
def adjust_tag_counts(current_song_tags,all_tags_with_counts):
    foundTag=False
    for current_song_tag in current_song_tags:
        for tag_with_count in all_tags_with_counts:
            if current_song_tag == tag_with_count:
                all_tags_with_counts[tag_with_count]=all_tags_with_counts[tag_with_count] + 1
                foundTag=True
                break
        if(foundTag == False):
            all_tags_with_counts[current_song_tag]=1
        foundTag=False

# Method to print the tags with the total of how often they appear in the music library to csv
def print_tag_counts_to_csv(all_tags_with_counts):
    tags_filename="/Users/kcingel/PycharmProjects/my_music_library_analysis/MusicLibraryTagCounts.csv"
    tags_file = open(tags_filename,"w")
    for tag_count in all_tags_with_counts:
        tags_file.write(tag_count[0] + "," + str(tag_count[1]) + "\n")
    tags_file.close()

API_KEY = "4d9b3cb29dbdb6d8b3c760c507c0ceb0"
API_SECRET = "d71a1d2bb2354bd1d6af3d6d129779da"

username="kcingel"
password_hash = pylast.md5("Don'tStealMyPwd1995!")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)
music_library_filename="/Users/kcingel/PycharmProjects/my_music_library_analysis/KaseysMusicLibrary.csv"


master_music_library_filename="/Users/kcingel/PycharmProjects/my_music_library_analysis/MasterMusicLibrary.csv"
master_music_library_file = open(master_music_library_filename,"w")

all_songs = {}

all_tags = []
# Keeps track of all the tags and the number of times they appear in my music library
# all_tags_with_counts={}

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
        except:
            print("Track " + song_name + " not found")
            continue;
        tags = parse_pylast_top_tags(pylast_tags)
        all_songs[song_name]['tags']=tags

        for tag in tags:
            all_tags.append(tag)
        # Add the current tags to the dictionary keeping track of all tag counts
        # adjust_tag_counts(tags,all_tags_with_counts)

        # Write the song name, artist, album and date the song was added to the music library to csv file
        master_music_library_file.write(song_name + ",")
        master_music_library_file.write(all_songs[song_name]['artist'] + ",")
        master_music_library_file.write(all_songs[song_name]['album'] + ",")
        master_music_library_file.write(all_songs[song_name]['added date'] + ",")

        # Write all the tags for the song to the music library
        length_song_tags = len(all_songs[song_name]['tags'])
        for i in range(0,length_song_tags):
            tag=tags[i]
            if(i==(length_song_tags-2)):
                master_music_library_file.write(tag)
            else:
                master_music_library_file.write(tag + ",")
        master_music_library_file.write('\n')

    master_music_library_file.close()
    all_tags_with_counts=Counter(all_tags)
    ordered_all_tags_with_counts = all_tags_with_counts.most_common()
    print_tag_counts_to_csv(ordered_all_tags_with_counts)
























