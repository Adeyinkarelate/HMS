from django.urls import path
from userauth.views import register_view


app_name = 'userauth'

urlpatterns = [
    path("sign-up/",register_view,name='sign-up'),
    
]