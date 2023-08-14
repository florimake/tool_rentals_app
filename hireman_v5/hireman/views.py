from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime as dt
from datetime import timedelta
from pprint import pprint




# Create your views here.



butoane = Buton_meniu.objects.all() 
# butoane_hardcodat = ["home", "category", "products", "details", "admin"]

time_date=timezone.now()

# Preluarea datei
# data = datetime.now().strftime("%Y-%m-%d")
data = datetime.date.today()
year = datetime.date.today().year
# month = str(datetime.date.today().strftime('%B'))
month = datetime.date.today().month
day = str(datetime.date.today().day).zfill(2)


############################################################## GLOBAL ################################################################

# Contracte incheiate in ultimile 10 zile harcodate
contracte = [contract for contract in Contract.objects.all()]


#lista cu 3 cele mai inchiriate produse
def cele_mai_inchiriate(index=None):
    contracte = Contract.objects.all()
    produse = {}
    # print([c.produs for c in contracte])
    for contract in contracte:
        produs = contract.produs
        if produs in [k for k, v in produse.items()]:
            produse[produs] += 1
        else:
            produse[produs] = 1
    sorted_keys = dict(sorted(produse.items(), key=lambda item:item[1], reverse=True))
    # pprint([(Produs.objects.get(slug=k),v) for k, v in sorted_keys.items()][0:3])
    if index == None:
        return [[Produs.objects.get(slug=k),v] for k, v in sorted_keys.items()][0:3]
    elif index != None:
        if index <= len([[Produs.objects.get(slug=k),v] for k, v in sorted_keys.items()]):
            return [[Produs.objects.get(slug=k),v] for k, v in sorted_keys.items()][0:index]
        else:
            xlen = len([[Produs.objects.get(slug=k),v] for k, v in sorted_keys.items()])
            print(f"\n<<< info >>> Valoarea introdusa ca parametru in >>> cele_mai_inchiriate({index}) este prea mare. Functia va returna maxim {xlen} produse\n")
            return [[Produs.objects.get(slug=k),v] for k, v in sorted_keys.items()][0:xlen]


# Global context care se aplica pentru toate paginile
request = None
CONTEXT_GLOBAL = {
        "request": request,
        "butoane": butoane,
        "year_now": year,
        "month_now": month,
        "day_now": day,
        "contracte_info": [c for c in Contract.objects.all() if data <= c.data_end][::-1][0:4],
        "contracte": contracte[::-1],
        "produse_populare": cele_mai_inchiriate(3),
    }


def add_first_to_second_dict(first_dict, second_dict):
    """  Aceasta functie are nevoie de doua dictionare:
    - concateneaza/adauga first_dict in second_dict
    - returneaza second_dict  """
    for key, value in first_dict.items():
        second_dict[key] = value
    return second_dict

#last contract
last_contract = {}
service_save = {}



    
    

############################################################## GLOBAL ################################################################


############################################################### MAIN #################################################################
def view_main(request):
    cele_mai_inchiriate()
    context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "main.html", context)
############################################################### MAIN #################################################################


############################################################# CATEGORY ###############################################################
def view_category(request):
    categorii = Categorie.objects.all()
    context = {
        "categorii": categorii,
    }
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "category.html", context)
############################################################# CATEGORY ###############################################################


############################################################# PRODUCTS ###############################################################
def view_products(request):
    cele_mai_inchiriate()
    global service_save, contracte
    contracte = [contract for contract in Contract.objects.all()]
    Reparatie.objects.get
    c = [x.Schimba_status_produs() for x in Contract.objects.all()][0]
    r = [r.stare_produs() for r in Reparatie.objects.all()][0]
    # print(f"c: {c}, r: {r}")
    
    if request.method == 'GET':
        rezultat = []
        get = request.GET
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
        
    elif request.method == "POST":
        post = request.POST
        print(post)
        print(service_save)
        reparatie = Reparatie(
            nume_service = post["nume_service"],
            tel = post["tel"],
            mail = post["mail"],
            produs_id = service_save["produs"],
            
            cost = post["cost"],
            # data = datetime.date(datetime.now()),
            data_start = post["data_start"],
            data_end = post["data_end"],
        )
        reparatie.stare_produs
        reparatie.save()
        produse = Produs.objects.all()
        context = {
            "produse": produse,
            "mesaj": "Search..."
        }
        
        add_first_to_second_dict(CONTEXT_GLOBAL,context)
        return render(request, "products.html", context)
        
############################################################# PRODUCTS ################################################################        
        

######################################################### PRODUCTS CATEGORY ###########################################################
def view_products_category(request, slug=None):
    global contracte
    contracte = [contract for contract in Contract.objects.all()]
    cele_mai_inchiriate()
    
    Reparatie.objects.get
    Contract.objects.get
    
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
######################################################### PRODUCTS CATEGORY ###########################################################

########################################################## PRODUCT DETAILS ############################################################
def view_product_details(request, slug=None):
    if slug != None:
        spec = get_object_or_404(Produs, slug=slug).specificatii
        produs_selectat = Produs.objects.get(slug=slug)
        
        # ferificare status si preluarea datei cand se termina perioada
        if produs_selectat.status == "disponibil" :
            add_first_to_second_dict({
                    "data_end": f" ",
                    "display": " ",
                }, CONTEXT_GLOBAL)
        elif produs_selectat.status == "nedisponibil" :
            data_end_contract = Contract.objects.get(pk = produs_selectat.pk).data_end
            print(data_end_contract)
            add_first_to_second_dict({
                    "data_end": f"Disponibil de pe {data_end_contract + timedelta(days=1)}",
                    "display": "display: none",
                }, CONTEXT_GLOBAL)
        elif produs_selectat.status == "service" :
            data_end_service = Reparatie.objects.get(produs_id = produs_selectat.pk).data_end
            print(data_end_service)
            add_first_to_second_dict({
                    "data_end": f"Disponibil de pe {data_end_service + timedelta(days=1)}",
                    "display": "display: none",
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
########################################################## PRODUCT DETAILS ############################################################


############################################################## DETAILS ################################################################
def view_details(request):
    global last_contract, contracte, month
        
    get = request.GET
    key_get = [k for k, v in get.items()]
    value_get = [v for k, v in get.items()]
    produse_afisate = 10
    produse_inchiriate = cele_mai_inchiriate(produse_afisate)
    
    contracte = [contract for contract in Contract.objects.all()]
    total_incasat_luna_curs = [x.cost for x in contracte if x.data_end.month == month]
    total_geberal = sum([x.cost for x in contracte])
    # pprint(total_incasat_luna_curs)
    contract_details = [x for x in contracte if x.data_end.month == month][::-1]
    context = {
            "mesaj": "",
            'produse_inchiriate':dict(produse_inchiriate).items(),
            'total_incasat': sum(total_incasat_luna_curs),
            'contract_details': contract_details[:14],
            'total_general': total_geberal,
            "srl" : Societate.objects.get(),
        }
    contracte = [c.Schimba_status_produs() for c in Contract.objects.all()][-1]
    # print(contracte)
    
    if len(key_get) > 0:
        print(f"Sa salvat: {key_get[0]} {value_get[0]}")    
        context = {
            "mesaj": f"Sa salvat cu succes: {key_get[0]} {value_get[0]}",
            'produse_inchiriate':dict(produse_inchiriate).items(),
            'total_incasat': sum(total_incasat_luna_curs),
            'contract_details': contract_details[:14],
            'total_general': total_geberal,
            "srl" : Societate.objects.get(),
        }
        # print(last_contract)
            
    if request.method == 'POST':
            rq = request.POST
            last_contract["banca_client"] = rq["banca"]
            last_contract["cont_client"] = rq["contul"]
            
            print(rq)
            print(rq["banca"], rq["contul"])
            # print([Contract.objects.get(all)])
            
            # Metoda de salvare in DB contract
            contract = Contract(
                nume_srl = last_contract["nume_srl"],
                cui = last_contract["cui"],
                adresa_srl = last_contract["adresa_srl"],
                director = last_contract["director"],
                tel_srl = last_contract["tel_srl"],
                mail_srl = last_contract["mail_srl"],
                banca_srl = last_contract["banca_srl"],
                cont_srl = last_contract["cont_srl"],
                
                # client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
                nume_client = last_contract["nume_client"],
                cnp = last_contract["cnp"],
                adresa_client = last_contract["adresa_client"],
                adresa_livrare = last_contract["adresa_livrare"],
                tel_client = last_contract["tel_client"],
                mail_client = last_contract["mail_client"],
                banca_client = last_contract["banca_client"],
                cont_client = last_contract["cont_client"],
                
                produs = Produs.objects.get(nume=last_contract["produs"]).slug,
                garantie_produs = last_contract["garantie_produs"],
                cost = last_contract["cost"],
                nr_zile = last_contract["nr_zile"],
                data_start = dt.strptime(f"{last_contract['data_start']}", '%d-%m-%Y').date(),
                data_end = dt.strptime(f"{last_contract['data_end']}", '%d-%m-%Y').date(),
            )
            # print(contract)
            
            contract.save()
            contract.Schimba_status_produs()
            context = {
                "mesaj": f"Sa salvat cu succes: Contractul nr. {contract.pk}",
                'produse_inchiriate':dict(produse_inchiriate).items(),
                'total_incasat': sum(total_incasat_luna_curs),
                'contract_details': contract_details[:14],
                'total_general': total_geberal,
                "srl" : Societate.objects.get(),
            }
    
            clienti = Client.objects.all()
            save = bool([x for x in clienti if x.cnp == int(last_contract["cnp"])])
            # print(save)
            if not save:
                client = Client(
                    nume = last_contract["nume_client"],
                    cnp = last_contract["cnp"],
                    adresa = last_contract["adresa_client"],
                    tel = last_contract["tel_client"],
                    mail = last_contract["mail_client"],
                )
                # print(client)
                client.save()
            cele_mai_inchiriate()
            last_contract = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "details.html", context)
############################################################## DETAILS ################################################################


############################################################### HOME ##################################################################
def view_home(request):
    global contracte
    contracte = [contract for contract in Contract.objects.all()]
    cele_mai_inchiriate()
    
    context = {}
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    return render(request, "home.html", context)
############################################################### HOME ##################################################################


########################################################## CLIENT DETAILS #############################################################
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
########################################################## CLIENT DETAILS #############################################################


########################################################## CONTRACT DETAILS ###########################################################
def view_contract_details(request, slug=None):
    cele_mai_inchiriate()
    global last_contract 
    # last_contract = {}
    td = time_date.date()
    
    # print(f" - Open view_contract_details() => succes")
    global data
    if slug != None:
        context = {}
        
        if request.method == 'POST':
            # print(f"- request POST => accepted")
            rq = request.POST
            data_start = request.POST["data_start"]
            dts = dt.strptime(f"{data_start[8:11]}-{data_start[5:7]}-{data_start[:4]}", '%d-%m-%Y').date()
            dte = dt.strptime(f"{data_start[8:11]}-{data_start[5:7]}-{data_start[:4]}", '%d-%m-%Y').date() + timedelta(days=int(request.POST["pret"][-2::1]))
            pret_total = int(request.POST["pret"][0:-3:1]) + int(get_object_or_404(Produs, slug=slug).garantie)
            mesaj = " ... nespecificat ..."
            print(f"Data start: {dts}")
            print(f"Data end: {dte}")
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
            
            societate = Societate.objects.get()
            produs = get_object_or_404(Produs, slug=slug)
            # print(societate, produs)
            add_first_to_second_dict({
                    #societatea
                "nr_contract": f"{len(Contract.objects.all()) + 1}",
                "nume_srl" : Societate.objects.get(),
                "cui": societate.cui,
                "adresa_srl": societate.adresa,
                "director": societate.director,
                "tel_srl": societate.tel,
                "mail_srl": societate.mail,
                "banca_srl": societate.banca,
                "cont_srl": societate.cont,
                    
                    #clientul
                "nume_client": request.POST["nume"] if len(request.POST["nume"])>1 else mesaj,
                "cnp": request.POST["cnp"] if len(request.POST["cnp"])>1 else mesaj,
                "adresa_client": request.POST["adresa"] if len(request.POST["adresa"])>1 else mesaj,
                "adresa_livrare": request.POST["adresa_livrare"] if len(request.POST["adresa_livrare"])>1 else request.POST["adresa"],
                "tel_client": request.POST["tel"] if len(request.POST["tel"])>1 else mesaj,
                "mail_client": request.POST["email"] if len(request.POST["email"])>1 else mesaj,
                "banca_client": "",
                "cont_client": "",
                    
                    #produsul
                "produs": produs.nume,
                "garantie_produs": produs.garantie,
                "cost" : pret_total,
                "nr_zile": request.POST["pret"][-2::1],
                "data_start": f"{dts.day}-{dts.month}-{dts.year}",
                "data_end": f"{dte.day}-{dte.month}-{dte.year}",
                }, last_contract)
            print(last_contract)
        # get = request.GET
        # key_get = [k for k, v in get.items()]
        # value_get = [v for k, v in get.items()]
        # add_first_to_second_dict(last_contract,context)
        
        # # Metoda de salvare in DB contract
        # if len(key_get) > 0:
        #     print(f"Sa salvat: {key_get[0]} {value_get[0]}")            
        
    else: 
        print(f"- request POST => not accepted")
        context = {}
        add_first_to_second_dict(CONTEXT_GLOBAL,context)
    
    # print(f" - Close view_contract_details() => succes")    
    # last_contract = context
    
    return render(request, "contract_details.html", context)
########################################################## CONTRACT DETAILS ###########################################################

##########################################################
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
###########################################################

######################################################### TERMENI CONTRACT ############################################################
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
######################################################### TERMENI CONTRACT ############################################################

######################################################### SERVICE DETAILS ############################################################
def view_service_details(request, slug=None):
    global service_save
    print(f" - Open view_service_details() => succes")
    if slug != None:
        print(f"- request POST => accepted")
        context = {
            "produs": get_object_or_404(Produs, slug=slug),
            "produs_pk": get_object_or_404(Produs, slug=slug).pk,
            "preturi": PretProdus.objects.all(),
            "time_date": f"{time_date.date()}",
        }
        print(context)
        add_first_to_second_dict(context, service_save)
        
    elif request.method == "POST":
        post = request.POST
        print(post)
    else: 
        context = {}
        print(f"- request POST => not accepted")
    add_first_to_second_dict(CONTEXT_GLOBAL,context)
    print(f" - Close view_service_details() => succes")
    return render(request, "service_details.html", context)
######################################################### SERVICE DETAILS ############################################################


############################################################## IMAGINE ################################################################
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
############################################################## IMAGINE ################################################################