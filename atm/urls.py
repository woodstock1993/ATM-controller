from django.urls import path, include
from atm import views

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),
]

