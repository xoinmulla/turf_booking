from django.urls import path
from . import views
from booking import views 
from .views import profile


urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:turf_id>/', views.book_turf, name='book_turf'),
    path('my_bookings/', views.booking_list, name='booking_list'),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', profile, name='profile'),
]
