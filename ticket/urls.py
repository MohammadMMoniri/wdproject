from django.urls import path

from ticket.views import ticket_detail_view, tickets_view, company_view

urlpatterns = [
    path("tickets/", tickets_view),
    path("tickets/<int:pk>/", ticket_detail_view),
    path("company/<int:pk>/", company_view),
]
