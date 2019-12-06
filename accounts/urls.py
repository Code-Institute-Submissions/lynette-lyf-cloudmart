from django.urls import path, include
from .views import index, logout, login, profile, register, view_transaction


urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/', profile, name='user_profile'),
    path('profile/<transaction_id>', view_transaction, name='view_transaction'),
    path('register/', register, name='user_register')
]