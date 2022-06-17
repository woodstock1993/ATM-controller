from django.urls import path, include
from atm import views

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),
    path('accounts/', views.AccountList.as_view()),
    path('accounts/<int:pk>', views.AccountDetail.as_view()),
    path('bank/<int:pk>', views.AccountBalanceDetail.as_view())
]

