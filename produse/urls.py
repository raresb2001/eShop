from django.urls import path

from produse import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('buy/<id>', views.change_status, name='change_status')
    ]

