from django.urls import path
from . import views

urlpatterns = [
    # name - w templatkach i widokach zebysmy mogli sie odwolac, np. action
    path('', views.home, name='home' ),
    # typ danych: nazwe zmienne, na koniec niepustej sciezki /
    path('<int:postId>/', views.detail, name='detail' ),

]
