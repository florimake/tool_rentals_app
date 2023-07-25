from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime as dt
from datetime import timedelta


# Create your views here.



butoane = Buton_meniu.objects.all() 
# butoane_hardcodat = ["home", "category", "products", "details", "admin"]

time_date=timezone.now()

# Preluarea datei
data = datetime.date.today()
year = datetime.date.today().year
# month = str(datetime.date.today().strftime('%B'))
month = datetime.date.today().month
day = str(datetime.date.today().day).zfill(2)




# Contracte incheiate in ultimile 10 zile harcodate
contracte = ["10", '11', '12', '13', '14']



# Global context care se aplica pentru toate paginile
request = None
CONTEXT_GLOBAL = {
        "request": request,
        "butoane": butoane,
        "data": data,
        "data_now": data,
        "year_now": year,
        "month_now": month,
        "day_now": day,
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

def view_client_details(request, slug=None):

    if slug != None:
        pret = get_object_or_404(Produs, slug=slug).pret
        context = {
        "produs": get_object_or_404(Produs, slug=slug) ,
        "preturi": PretProdus.objects.all(),
        }
        
    else: 
        context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "client_details.html", context)

# def view_contract_details(request):
#     if request.method == 'POST':
#             print(f"A primit request POST")
#     context = {}
#     add_first_to_second_dict(CONTEXT_GLOBAL,context)
#     return render(request, "contract_details.html", context)

def view_contract_details(request, slug=None):
    if slug != None:
        context = {}
        if request.method == 'POST':
            # print(f"A primit request POST")
            r = request.POST
            data_start = request.POST["data_start"]
            date_end = time_date + timedelta(days=int(request.POST["pret"][-2::1]))
            pret_total = int(request.POST["pret"][0:-3:1]) + int(get_object_or_404(Produs, slug=slug).garantie)
            # print(date_end.date())
            # print(type(int(day)))
            # print(pret_total)
            context = {
            "produs": get_object_or_404(Produs, slug=slug) ,
            "preturi": PretProdus.objects.all(),
            "forms":r.items(),
            "nume": request.POST["nume"],
            "cnp": request.POST["cnp"],
            "adresa": request.POST["adresa"],
            "telefon": request.POST["tel"],
            "mail": request.POST["email"],
            "data_start": f"{data_start[8:11]} - {data_start[5:7]} - {data_start[:4]}",
            "data_end": f"{date_end.date().day} - {date_end.date().month} - {date_end.date().year}",
            "pret": request.POST["pret"][0:-3:1],
            "zile": request.POST["pret"][-2::1],
            "total_plata" : pret_total
            }
            add_first_to_second_dict(CONTEXT_GLOBAL,context)
    else: 
        context = {}
        add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "contract_details.html", context)

###################################################################
# def index(request):
#       return render(request, 'index.html')
# def validate(request):
#    if request.method == 'POST':
#       username= request.POST["user"]
#       password = request.POST["pass"]
#       dict = {
#          'username': username,
#          'password': password
#       }
#       return render(request, 'validate.html', dict) 
###################################################################