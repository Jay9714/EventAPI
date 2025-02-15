from django.urls import path
from event_api import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('events/', views.EventView.as_view(), name='events'),
    path('events/<int:event_id>/purchase/', views.TicketView.as_view(), name='TicketView')
]