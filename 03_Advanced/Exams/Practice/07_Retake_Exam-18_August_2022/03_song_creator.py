def add_songs(*args):
    songs = {}

    for info in args:
        if info[0] not in songs:
            songs[info[0]] = []

        songs[info[0]].extend(info[1])

    result = []

    for s, lyrics in songs.items():
        result.append(f"- {s}")
        result.extend(lyrics)

    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
