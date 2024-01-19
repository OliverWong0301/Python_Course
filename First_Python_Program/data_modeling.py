# SPOTIFY example:

playlist = {

    "name": "My Playlist",
    "author": "Oliver",
    "songs": [
        {"title": "Hello", "artist": ["Adele"], "duration": 3.38},
        {"title": "Forever", "artist": ["Drake", "Kanye West", "Eminem", "Lil Wayne"], "duration": 2.38},
        {"title": "Shivers", "artist": ["Ed Sheeran"], "duration": 5.38},
        {"title": "Angel Baby", "artist": ["Troye Sivan"], "duration": 2.38},
        {"title": "Take on Me", "artist": ["Mia Amare", "Sarah Bird"], "duration": 6.38},
        {"title": "Hello", "artist": ["Adele"], "duration": 4.53},
    ]

}

# Print all the songs name in playlist:
for song in playlist["songs"]:
    print(f"All the playlist songs are: {song["title"]}")
    print("All the playlist songs are: ", song["title"])

# Sum all the total duration of the playlist:
total_duration = 0
for song in playlist["songs"]:
    total_duration += song["duration"]
    print(total_duration) # Put here to see increment of duration until the last one as the total one || means this line of code is still in the loop
print(total_duration) # Put here to quit the loop then you'll have the total duration in one line