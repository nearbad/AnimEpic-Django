from pathlib import Path
import requests

from main.models import Character

with open("scripts/names.txt", encoding='utf-8') as file:
    name_of_person = file.readlines()
bio_of_person = [w for w in Path("scripts/bios.txt").read_text(encoding="utf-8").replace('\n', '').split('----')]
with open('scripts/photos.txt', encoding='utf-8') as file2:
    photo_of_person = file2.readlines()

n = 0
for each in name_of_person:
    try:
        person = Character()
        person.name = each.strip()
        person.slug = each.strip().replace(' ', '-').replace('\'', '')
        person.content = bio_of_person[n]
        p = requests.get(photo_of_person[n])
        out = open(fr"media\photos\2023\01\31\img_{person.slug}.jpg", "wb")
        out.write(p.content)
        person.photo = fr'photos\2023\01\31\img_{person.slug}.jpg'
        out.close()
        person.cat_id = 2
        n += 1
        person.save()

    except:
        continue
