from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(PretProdus)
admin.site.register(Client)
admin.site.register(Societate)
admin.site.register(Cos)


# @admin.register(MeniuBar)
# class MeniuBarAdmin(admin.ModelAdmin):
#     list_display = ("name", )
#     prepopulated_fields = {"slug": ("name",)}


@admin.register(Buton_meniu)
class Buton_meniuAdmin(admin.ModelAdmin):
    list_display = ("buton", )
    prepopulated_fields = {"slug": ("buton",)}

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("categorie", )
    prepopulated_fields = {"slug": ("categorie",)}

@admin.register(Produs)
class ProdusAdmin(admin.ModelAdmin):
    list_display = ("nume", "categorie", "status", "cod_produs", "pret", "garantie")
    list_filter = ("status", "categorie",)
    prepopulated_fields = {"slug": ("nume","cod_produs",)}
    search_fields = ("nume", "cod_produs", "status")
    

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("__str__" , "nume_client", "produs", Contract.Schimba_status_produs, Contract.perioada, "data_start", "data_end", Contract.Status)
    list_filter = ("data",)
    search_fields = ("data_start",)
    
@admin.register(Recenzie)
class RecenzieAdmin(admin.ModelAdmin):
    # _stars = type("stars")
    list_display = ('user', "__str__" , 'produs')

@admin.register(Reparatie)
class ReparatieAdmin(admin.ModelAdmin):
    list_display = ('produs_id', "data_start" , 'data_end', 'cost')