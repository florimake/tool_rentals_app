from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
import datetime

# Create your views here.



butoane = Buton_meniu.objects.all() 
# butoane_hardcodat = ["home", "category", "products", "details", "admin"]



# Preluarea datei
data = datetime.datetime.now().date



# Contracte incheiate in ultimile 10 zile harcodate
contracte = ["10", '11', '12', '13', '14']



# Global context care se aplica pentru toate paginile
request = None
CONTEXT_GLOBAL = {
        "request": request,
        "butoane": butoane,
        "data": data,
        "contracte": contracte,
    }


def add_first_to_second_dict(first_dict, second_dict):
    """  Aceasta functie are nevoie de doua dictionare:
    - concateneaza/adauga first_dict in second_dict
    - returneaza second_dict  """
    for key, value in first_dict.items():
        second_dict[key] = value
    return second_dict



def view_main(request):
    context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "main.html", context)


def view_category(request):
    categorii = Categorie.objects.all()
    context = {
        "categorii": categorii,
    }
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "category.html", context)


def view_products(request):
    produse = Produs.objects.all()
    context = {"produse": produse}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "products.html", context)

def view_products_category(request, slug=None):
    
    produse = []
    produse_cat = Produs.objects.all()
    # print(produse_cat)
    for x in produse_cat:
        if x.categorie.slug == slug:
            # print(x)
            produse.append(x)

    context = {"produse": produse,
               "categoria": Categorie.objects.get(slug=slug)
               }
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "products_category.html", context)

def view_product_details(request, slug=None):

    if slug != None:
        spec = get_object_or_404(Produs, slug=slug).specificatii
        context = {
        "produs": get_object_or_404(Produs, slug=slug) ,
        "preturi": PretProdus.objects.all(),
        "specificatii": spec.splitlines()
        }
        
    else: 
        context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    
    
    return render(request, "product_details.html", context)


def view_details(request):
    context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "details.html", context)


def view_home(request):
    context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "home.html", context)