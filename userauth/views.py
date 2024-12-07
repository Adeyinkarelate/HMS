from django.shortcuts import render, redirect
from django.contrib import messages
from userauth.forms import UserRegistrationForm , LoginForm
from django.contrib.auth import authenticate, login

from doctor import models as doctor_model
from patient import models as patient_model
from userauth import models as user_model


def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect("/")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save user instance but not to DB yet
            full_name = form.cleaned_data.get("full_name")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            user_type = form.cleaned_data.get("user_type")

            user.set_password(password1)  # Ensures password is properly hashed
            user.save()

            # Authenticate the user
            authenticated_user = authenticate(request, email=email, password=password1)

            if authenticated_user is not None:
                login(request, authenticated_user)

                # Create associated profile based on user_type
                if user_type == "Doctor":
                    doctor_model.Doctor.objects.create(user=authenticated_user, full_name=full_name)
                else:  # Assume "Patient" as default
                    patient_model.Patient.objects.create(user=authenticated_user, full_name=full_name, email=email)

                messages.success(request, "Account created successfully")
                return redirect("/")
            else:
                messages.error(request, "Authentication failed. Please try logging in.")
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, "userauth/sign-up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect("/")
    
    if request.method == "POST":
        form =  UserRegistrationForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data("email")
            password = form.cleaned_data("password")
            
            
            try:
                user_instance = user_model.User.objects.get(email=email ,is_valid=True)
                user_authenticate = authenticate(request,email=email,password=password)
                
                if user_instance is not None:
                    login(request,user_authenticate)
                    messages.success(request, "Account created successfully")
                    
                
                    next_url = request.GET.get("next","/")
                    return redirect(next_url)
                else:
                    messages.error(request, "Please correct the errors in the form.")
            except:
                messages.error(request, "User does not exist.")
            
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    return render(request, "userauth/sign-up.html", context)

            