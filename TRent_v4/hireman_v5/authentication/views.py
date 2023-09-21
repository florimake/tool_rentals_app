from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from hireman_v5 import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage
from hireman import models

# Create your views here.


def home(request):
    return render ( request, 'authentication/index.html')

def signup(request):
    """
    Verificam daca exista un submit de tip POST
    """
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1= request.POST ['pass1']
        pass2 =  request.POST ['pass2']
        
        """
        Metoda de verificare daca userul exista
        Daca exista ne redirectioneaza la home page pentru a reintroduce
        """
        if User.objects.filter(username=username):
            # messages.info(request,'Username already exists!')
            messages.error(request,'Utilizatorul exista deja!')
            return redirect("authentication/signin")
        
        """
        Metoda de verificare daca emailul exista
        Daca exista ne redirectioneaza la home page pentru a reintroduce
        """
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists!")
            return redirect("/home")
        
        if len(username) > 10:
            messages.error(request,"Username must be less than or equal to 10 characters.")

        if pass1 != pass2:
            messages.error(request,"Passwords do not match! Please try again...")
            
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-numeric!")
            return redirect("/home")
        
        

        # Creiem un obiect de tip User
        myuser = User.objects.create_user(username, email, pass1)
        # salvam in baza de date
        myuser.is_active = False
        myuser.save()
        
        # returneaza un mesaj de confirmare
        messages.success(request, "Contul a fost creiat cu succes.\n Va rog sa confirmati adresa de E-mail pentru a va activa contul.")
        
        ### Welcome Email
        subject = "Welcome to ToolRent site"
        message = f"Salut {myuser.username},\n Acesta este un mail de confirmarea creierii contului pe Tool Rent Site.\n In scurt timp o sa primiti un mail de confirmarea adresei dumneavoastra de email, va rog sa confirmati prin accesarea link-ului de activare. \n\nVa mmultumesc!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        
        # pip install django-email
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # messages.success(request, 'Send mail!')
        
        ### Email address Confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirma email-ul pentru inregistrarea pe ToolRent !!!"
        message2 = render_to_string(
            'email_confirmation.html', 
                {
                'name': myuser.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)
                }
            )
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        
        
        
        ### ne redirectioneaza pe pagina de logare
        return redirect('/signin')
    
    return render ( request, 'authentication/signup.html', {"srl": models.Societate.objects.get(),})

def signin(request):
    # arpad.python.test.app@gmail.com
    print(request.method)
    if request.method == "POST":
        username = request.POST['username']
        pass1= request.POST ['pass1']
        
        user = authenticate(username=username , password=pass1)
        print(user)
        if user is not None:
            login(request, user )
            user_name = user.get_username
            print(user_name)
            response={
                'name':user_name,
            }
            return redirect("/home")
            # return render(request, "home.html", response)
        else:
            messages.error(request, f"Utilizatorul {username} nu exista, creiaza unul")
            return redirect("authentication/signup")
    
    return render ( request, 'authentication/signin.html', {"srl": models.Societate.objects.get(),})

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("/home")

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('/home')
    else:
        return render(request, 'activation_failed,html')
    