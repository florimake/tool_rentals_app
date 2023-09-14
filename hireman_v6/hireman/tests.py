from django.test import TestCase
# from django.conf import settings

# settings.configure()

# from models import Produs

# class ProdusTestCase(TestCase):
    
#     print(Produs.objects.all())
#     print(Produs.status == "disponibil")


# Create your tests here.
CONTEXT_GLOBAL = {
    "buanee": 4,
        "quwest": 25,
        "daa": 3,
        "contacte": 12,
    }

print(CONTEXT_GLOBAL)

context2 = {
        "butoanee": 3,
        "requwest": 5,
        "datwa": 23,
        "contwracte": 1,
    }

print(context2)


def concatenate_dict(first_dict, second_dict):
    """
    Aceasta functie are nevoie de doua dictionare:
    - concateneaza first_dict cu second_dict
    - returneaza un dictionar 
    
    """
    for x, y in first_dict.items():
        second_dict[x] = y
    return second_dict

def concatenate_dict2(*args):
    """ - Aceasta functie concateneaza doua sau mai multe dictionare
    - Daca cheia exista se updateaza cheia
    - Returneaza un singur dictionar """
    second_dict = {}
    for d in args:
        print(d)
        for x, y in d.items():
            second_dict[x] = y
    return second_dict

concat = concatenate_dict(context2, CONTEXT_GLOBAL)

print(concat)
help(concatenate_dict)
    