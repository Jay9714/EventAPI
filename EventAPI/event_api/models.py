from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    user_role = models.CharField(max_length=10, choices=USER_ROLES, default='User')
    
    def __str__(self):
        return self.username


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    total_tickets = models.IntegerField(null=True, blank=True)
    tickets_sold = models.IntegerField(default=0)


class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)