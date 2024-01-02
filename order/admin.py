from django.contrib import admin

from order.models import ShoppingOrder, TicketCountOrder


@admin.register(ShoppingOrder)
class ShoppingOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(TicketCountOrder)
class BookCountOrderAdmin(admin.ModelAdmin):
    pass
