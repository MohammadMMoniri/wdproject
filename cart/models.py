from django.contrib.auth.models import User
from django.db import models

from ticket.models import Ticket


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BookCountCart(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
