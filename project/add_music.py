import json

def add_music():
filename = 'music.json'
try:
    with open("music.json", "w") as f:
        music = json.load(f)
except:
    name = input("Add name of song")
    with open(music.json, 'w') as m:
        json.dump(name, m)
        print("Add to list" + name)
    peoples = input("add name of band")
    with open(music.json, 'w') as t:
        json.dump(peoples, t)
        print("Add to list" + peoples)
    year = input("add year of song")
    with open(music.json, 'w') as y:
        json.dump(year, y)
        print("Add to list" + year)
    albums = input("add albums")
    with open(music.json, 'w') as a:
        json.dump(albums, a)
        print("Add to list" + albums)
else:
    print("your music" + music)

add_music()
