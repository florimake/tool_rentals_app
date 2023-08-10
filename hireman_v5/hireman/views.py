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

def cele_mai_inchiriate():
    pass

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
    if request.method == 'GET':
        rezultat = []
        get = request.GET
        print(len(get))
        print(len(rezultat))
        if len(get) > 0:
            for key, value in get.items():
                rezultat.append(value)
            
            produse = Produs.objects.all()
            produse_cautate=[]
            
            for produs in produse:
                if produs.status == rezultat[0]:
                    produse_cautate.append(produs)
                elif rezultat[0].lower() in produs.nume.lower() and len(get) > 0:
                    produse_cautate.append(produs)
                elif rezultat[0].lower() in produs.descriere.lower():
                    produse_cautate.append(produs)
            
            if len(produse_cautate) > 0 and len(get) == 1 and len(rezultat[0]) > 0:
                mesaj= f"{rezultat[0]}..."
            elif len(produse_cautate) == 0 and len(get) > 0:
                mesaj= f"{rezultat[0]}..."
            elif len(get) != 0:
                mesaj="Search..."
                
            context = {
                "produse": produse_cautate,
                "mesaj":mesaj
            }
            add_first_to_second_dict(CONTEXT_GLOBAL,context)
            return render(request, "products.html", context)
        
        else:
            produse = Produs.objects.all()
            context = {
                "produse": produse,
                "mesaj": "Search..."
            }
            add_first_to_second_dict(CONTEXT_GLOBAL,context)
            return render(request, "products.html", context)

def view_products_category(request, slug=None):
    
    produse = []
    produse_cat = Produs.objects.all()
    
    # print(produse_cat)
    for x in produse_cat:
        if x.categorie.slug == slug and x.status == "disponibil":
            print(x)
            produse.append(x)

    context = {
        "produse": produse,
        "categoria": Categorie.objects.get(slug=slug)
    }
    print(produse)
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "products_category.html", context)

def view_product_details(request, slug=None):
    if slug != None:
        spec = get_object_or_404(Produs, slug=slug).specificatii
        produs_selectat = Produs.objects.get(slug=slug)
        
        # ferificare status si preluarea datei cand se termina perioada
        if produs_selectat.status == "disponibil" :
            add_first_to_second_dict({
                    "data_end": f" "
                }, CONTEXT_GLOBAL)
        elif produs_selectat.status == "nedisponibil" :
            data_end_contract = Contract.objects.get(produs = produs_selectat.slug).data_end
            print(data_end_contract)
            add_first_to_second_dict({
                    "data_end": f"Disponibil de pe {data_end_contract + timedelta(days=1)}"
                }, CONTEXT_GLOBAL)
        elif produs_selectat.status == "service" :
            data_end_service = Reparatie.objects.get(produs_id = produs_selectat.id).data_end
            print(data_end_service)
            add_first_to_second_dict({
                    "data_end": f"Disponibil de pe {data_end_service + timedelta(days=1)}"
                }, CONTEXT_GLOBAL)
            
        print(f'product_details: {produs_selectat}')
        
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
    print(f" - Open view_client_details() => succes")
    if slug != None:
        print(f"- request POST => accepted")
        context = {
            "produs": get_object_or_404(Produs, slug=slug) ,
            "preturi": PretProdus.objects.all(),
            "time_date": f"{time_date.date()}",
        }
        
    else: 
        context = {}
        print(f"- request POST => not accepted")
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    print(f" - Close view_client_details() => succes")
    return render(request, "client_details.html", context)


last_contract = {}
def view_contract_details(request, slug=None):
    global last_contract
    
    print(f" - Open view_contract_details() => succes")
    global data
    if slug != None:
        context = {}
        
        if request.method == 'POST':
            print(f"- request POST => accepted")
            td = time_date.date()
            rq = request.POST
            data_start = request.POST["data_start"]
            data_end = dt.strptime(f"{data_start[8:11]}-{data_start[5:7]}-{data_start[:4]}", '%d-%m-%Y').date() + timedelta(days=int(request.POST["pret"][-2::1]))
            dts = dt.strptime(f"{data_start[8:11]}-{data_start[5:7]}-{data_start[:4]}", '%d-%m-%Y').date()
            dte = data_end
            pret_total = int(request.POST["pret"][0:-3:1]) + int(get_object_or_404(Produs, slug=slug).garantie)
            mesaj = " ... nespecificat ..."
            print(f"Data end: {data_end}")
            context = {
                "nr_contract": f"{len(Contract.objects.all()) + 1}",
                "srl" : Societate.objects.get(),
                "produs": get_object_or_404(Produs, slug=slug) ,
                "preturi": PretProdus.objects.all(),
                "forms":rq.items(),
                "nume": request.POST["nume"] if len(request.POST["nume"])>1 else mesaj,
                "cnp": request.POST["cnp"] if len(request.POST["cnp"])>1 else mesaj,
                "adresa": request.POST["adresa"] if len(request.POST["adresa"])>1 else mesaj,
                "adresa_livrare": request.POST["adresa_livrare"] if len(request.POST["adresa_livrare"])>1 else request.POST["adresa"],
                "telefon": request.POST["tel"] if len(request.POST["tel"])>1 else mesaj,
                "mail": request.POST["email"] if len(request.POST["email"])>1 else mesaj,
                "data_start": f"{dts.day}-{dts.month}-{dts.year}",
                "data_end": f"{dte.day}-{dte.month}-{dte.year}",
                "pret": request.POST["pret"][0:-3:1],
                "zile": request.POST["pret"][-2::1],
                "total_plata" : pret_total,
                "time_date": f"{td.day}-{td.month}-{td.year}",
                "data": f"{time_date.date()}",
            }
            add_first_to_second_dict(CONTEXT_GLOBAL,context)
    else: 
        print(f"- request POST => not accepted")
        context = {}
        add_first_to_second_dict(CONTEXT_GLOBAL,context)
    
    # print(f" - Close view_contract_details() => succes")    
    last_contract = context
    # print(last_contract)
    return render(request, "contract_details.html", context)

###################################################################
# Model de POST si GET
# 
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

def view_termeni_contract(request, slug=None):
    print(f" - Open view_termeni_contract() => succes") 
    if slug != None:
        pret = get_object_or_404(Produs, slug=slug).pret
        context = {
            "produs": get_object_or_404(Produs, slug=slug) ,
            "preturi": PretProdus.objects.all(),
        }
        
    else: 
        context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "termeni_contract.html", context)


def view_imagine(request, poza):
    produse = Produs.objects.all()
    category = Categorie.objects.all()
    img = ""
    for x in produse:
        if x.poza == f"hireman/static/media/{poza}":
            img = x
    for x in category:
        if x.poza == f"hireman/static/media/category/{poza}":
            img = x
    context= {
        "img_view" : img,
        }
    print(poza)
    print(img)
    return render(request, "img.html", context)
