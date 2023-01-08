from django import forms
from .models import Signup,Signin
class Signupform(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'enter your name','class':'c1'}),
            'email':forms.TextInput(attrs={'placeholder':'enter your email','class':'c1'}),

            'username':forms.TextInput(attrs={'placeholder':'enter your username','class':'c1'}),
            'password':forms.PasswordInput(attrs={'placeholder':'enter your password','class':'c1'})
        }

        labels={
            'name':'',
            'email':'',
            'username':'',

            'password':''
        }



class Signinform(forms.ModelForm):
    class Meta:
        model=Signin
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'enter your username','class':'c1'}),
            'password':forms.PasswordInput(attrs={'placeholder':'enter your password','class':'c1'})
        }

        labels={
            'username':'',
            'password':''
        }