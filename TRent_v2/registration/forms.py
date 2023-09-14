from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 
class SingUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update ({
            'requaired':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-input',
            'placeholder':'username',
            'maxlenght':'22',
            'minlenght':'8'
        })
        self.fields["email"].widget.attrs.update ({
            'requaired':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder':'arpad@mail.com',
            'maxlenght':'22',
            'minlenght':'8'
        })
        self.fields["password1"].widget.attrs.update ({
            'requaired':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-input',
            'placeholder':'password',
            'maxlenght':'22',
            'minlenght':'8'
        })
        self.fields["password2"].widget.attrs.update ({
            'requaired':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'form-input',
            'placeholder':'password',
            'maxlenght':'22',
            'minlenght':'8'
        })
        
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update ({
            'requaired':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder':'arpad@mail.com',
            'maxlenght':'22',
            'minlenght':'8'
        })
        
        self.fields["password1"].widget.attrs.update ({
            'requaired':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-input',
            'placeholder':'password',
            'maxlenght':'22',
            'minlenght':'8'
        })
        
        
    class Meta:
        model = User
        fields = ("email", "password1")
        
class ForgotPasswordForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update ({
            'requaired':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder':'arpad@mail.com',
            'maxlenght':'22',
            'minlenght':'8'
        })
    class Meta:
        model = User
        fields = ("email", )