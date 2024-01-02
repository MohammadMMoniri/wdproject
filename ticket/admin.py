from django.contrib import admin

from ticket.models import Ticket, Company


class BookPublisherInline(admin.StackedInline):
    model = Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("source", "create_date", "last_update")
    search_fields = ("source", "year")
    readonly_fields = ("last_update",)


@admin.register(Company)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookPublisherInline]
