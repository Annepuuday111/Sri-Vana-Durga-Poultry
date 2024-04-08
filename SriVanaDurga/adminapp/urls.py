from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='home.html'), name='home'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('home/', LoginView.as_view(template_name='home.html'), name='home'),
    path('checkadminlogin/', views.checkadminlogin, name='checkadminlogin'),

    path('addfeed/', views.addfeed, name='addfeed'),
    path('addmortality/', views.addmortality, name='addmortality'),
    path('addchicks/', views.addchicks, name='addchicks'),
    path('addmedicine/', views.addmedicine, name='addmedicine'),
    path('addvaccine/', views.addvaccine, name='addvaccine'),
    path('addlifting/', views.addlifting, name='addlifting'),

    path('viewfeed/', views.viewfeed, name='viewfeed'),
    path('viewchicks/', views.viewchicks, name='viewchicks'),
    path('viewmortality/', views.viewmortality, name='viewmortality'),
    path('viewmedicine/', views.viewmedicine, name='viewmedicine'),
    path('viewlifting/', views.viewlifting, name='viewlifting'),
    path('viewlifting/box_wise_data/', views.box_wise_data, name='box_wise_data'),
]
