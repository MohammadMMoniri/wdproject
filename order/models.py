from django.contrib.auth.models import User
from django.db import models

from ticket.models import Ticket


class ShoppingOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    finalize = models.BooleanField(default=False)

    @property
    def total_price(self):
        sum_price = 0
        for ticket_count in self.order_ticket_count.all():
            sum_price += ticket_count.count * ticket_count.ticket.price
        return sum_price


class TicketCountOrder(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(
        ShoppingOrder, on_delete=models.CASCADE, related_name="order_ticket_count"
    )
