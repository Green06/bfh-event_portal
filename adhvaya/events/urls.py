from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name = 'home'),
    # path('login/',views.home, name = 'login'),
    # path('signup/',views.home, name = 'signup'),

     path('',views.home),
    path('login/',views.home),
    path('signup/',views.home),
        

]