from django.urls import path
from booking.views import HomeView, BookingView, BookView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('booking/', BookingView, name='booking'),
    path('book/', BookView, name='bookpage'),
]
