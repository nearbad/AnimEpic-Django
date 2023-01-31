from main.models import Character


def run():
    char_list = Character.objects.all()
    for char in char_list:
        char.is_published = True
        char.save()







