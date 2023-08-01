from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Buton_meniu(models.Model):
    
    buton = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Buton'
        verbose_name_plural = 'Butoane'
        
    def __str__(self) -> str:
        return self.slug


class Categorie(models.Model):
    categorie = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    poza = models.ImageField(upload_to='hireman/static/media/category', null=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categori'
        verbose_name_plural = 'Categorii'

    def __str__(self) -> str:
        return self.categorie
    

class PretProdus(models.Model):
    pret_1 = models.IntegerField()
    pret_2 = models.IntegerField()
    pret_3 = models.IntegerField()
    pret_4 = models.IntegerField()
    pret_5 = models.IntegerField()
    pret_w = models.IntegerField() #pentru sanbata si duminica
    pret_s = models.IntegerField()
    data = datetime.date(datetime.now())

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Pret'
        verbose_name_plural = 'Preturi'
        
    def __str__(self) -> str:
        return f"{self.pret_1}"


class Produs(models.Model):
    categorie = models.ForeignKey(Categorie, serialize=True, on_delete=models.CASCADE)
    nume = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    cod_produs = models.IntegerField()
    descriere = models.TextField()
    specificatii = models.TextField()
    pret = models.ForeignKey(PretProdus, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=(("disponibil", "disponibil"), ("nedisponibil", "nedisponibil"), ("service", "service")), default="disponibil", max_length=20)
    poza = models.ImageField(upload_to='hireman/static/media/', null=True)
    garantie = models.IntegerField(default=600)
    data = datetime.date(datetime.now())
    
    def status_color(self):
        if self.status == "disponibil":
            return "green"
        elif self.status == "nedisponibil":
            return "red"
        elif self.status == "service":
            return "orange"
        else:
            return "black"
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Produs'
        verbose_name_plural = 'Produse'

    def __str__(self):
        return f"{self.nume}"
        


class Reparatie(models.Model):
    nume_service = models.CharField(max_length=50)
    tel = models.IntegerField()
    mail = models.CharField(max_length=50)
    produs_id = models.ForeignKey(Produs , on_delete=models.CASCADE, serialize=True) 
    
    cost = models.IntegerField()
    data = datetime.date(datetime.now())
    data_start = models.DateField(default= datetime.date(datetime.now()))
    data_end = models.DateField(default= datetime.date(datetime.now()))

    def stare_produs(self):
        data_curenta = datetime.date(datetime.now())
        stare = Produs.objects.get(nume=self.produs_id)
    
        if data_curenta < self.data_end and data_curenta >= self.data_start:
            stare.status = "service"
            stare.save()
    
        elif data_curenta > self.data_end:
            stare.status = "disponibil"
            stare.save()
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Reparatie'
        verbose_name_plural = 'Reparatii'
    
    def __str__(self) -> str:
        self.stare_produs()
        return f"{self.produs_id}"


class Cos(models.Model):
    produs_id = ""
    pret_id = 0
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cos'
        verbose_name_plural = 'Cosuri'
    
    def __str__(self) -> str:
        return self.produs_id.nume


class Client(models.Model):
    nume = models.CharField(max_length=50)
    cnp = models.IntegerField(null=True)
    adresa = models.CharField(max_length=150)
    tel = models.IntegerField()
    mail = models.CharField(max_length=50, null=True)
    data = datetime.date(datetime.now())
    # cos = models.ForeignKey(Cos, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clienti'
    
    def __str__(self) -> str:
        return self.nume


class Recenzie(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    stars = models.CharField(choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")), default=5, max_length=2)
    coment = models.TextField()
    data = datetime.date(datetime.now())

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Recenzie'
        verbose_name_plural = 'Recenzii'
    
    def __str__(self):
        return f"{int(self.stars) * ' ★ '}"
    
    



class Societate(models.Model):
    nume = models.CharField(max_length=50)
    ro = models.IntegerField()
    cui = models.IntegerField()
    adresa = models.CharField(max_length=150)
    director = models.CharField(max_length=50)
    tel = models.BigIntegerField()
    mail = models.CharField(max_length=50)
    data = datetime.date(datetime.now())
    banca = models.CharField(max_length=50, null=True)
    cont = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Societate'
        verbose_name_plural = 'Societati'
    
    def __str__(self) -> str:
        return self.nume


class Contract(models.Model):
    nr_contract = models.IntegerField(null=True, default=0)
    data = models.DateField(default= timezone.now(), null=True)
    
    # id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    
    # societate = models.ForeignKey(Societate, on_delete=models.CASCADE)
    nume_srl = models.CharField(max_length=50)
    cui = models.IntegerField()
    adresa_srl = models.CharField(max_length=150)
    director = models.CharField(max_length=50)
    tel_srl = models.BigIntegerField()
    mail_srl = models.CharField(max_length=50)
    banca_srl = models.CharField(max_length=50, null=True)
    cont_srl = models.CharField(max_length=50, null=True)
    
    # client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    nume_client = models.CharField(max_length=50)
    cnp = models.IntegerField()
    adresa_client = models.CharField(max_length=150)
    adresa_livrare = models.CharField(max_length=150)
    tel_client = models.BigIntegerField()
    mail_client = models.CharField(max_length=50)
    banca_client = models.CharField(max_length=50, null=True)
    cont_client = models.CharField(max_length=50, null=True)
    
    produs = models.CharField(max_length=50)
    garantie_produs = models.IntegerField()
    cost = models.IntegerField()
    nr_zile = models.IntegerField()
    data_start = models.DateField()
    data_end = models.DateField()
    
    # ZILE = (("1", "1 zi"), ("2", "2 zile"), ("3", "3 zile"), ("4", "4 zile"), ("5", "5 zile"), ("w", "weekend"), ("s", "o saptamana"))
    # perioada = models.CharField(choices=ZILE, default=1, max_length=50)
    def perioada(self):
        zile = (self.data_end - self.data_start)
        return zile.days
    
    observatii = models.CharField(max_length=255, null=True, default="fara observatii")
    
    def Status(self):
        data2 = datetime.date(datetime.now())
        if data2 < self.data_start:
            return f"Programat la {self.data_start}"
        elif data2 == self.data_start or (self.data > self.data_start and self.data <= self.data_end):
            return f"Se deruleaza"
        elif data2 > self.data_end:
            return f"Finalizat"
        else:
            return"null"
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracte'
    
    def __str__(self):
        self.Status()
        return f"Contract nr.{self.nr_contract} din {self.data}" 
    
    
# class MeniuBar(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField()
    
#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'meniu'
#         verbose_name_plural = 'meniuri'