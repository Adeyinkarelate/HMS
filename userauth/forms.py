from django import forms 
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User


    


class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"John Wu"}))  # this as just included
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"johnDoe@gmail.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"**************"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"**************"}))
    
    class Meta:
        model = User
        fields = ['full_name','email','password1','password2','user_type']
        
        
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"johnDoe@gmail.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"**************"}))
    
    class Meta:
        model = User
        fields = ['email','password1']
        
        

    """
    NB: if you are using tailwind, you can create a variable at the top and pass the stylying ...e.g
    
    # Define the Tailwind classes once
    TAILWIND_INPUT_CLASSES = "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":TAILWIND_INPUT_CLASSES,"placeholder":"johnDoe@gmail.com"}))
    """