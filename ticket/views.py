from django.http import HttpResponse
from django.template import loader

from ticket.models import Ticket, Company


def tickets_view(request):
    tickets = Ticket.objects.all()
    content = {"ticket": tickets}
    templates = loader.get_template("product/tickets.html")
    return HttpResponse(templates.render(content, request))


def ticket_detail_view(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    content = {"ticket": ticket}
    templates = loader.get_template("product/ticket_detail.html")
    return HttpResponse(templates.render(content, request))


def company_view(request, pk):
    company = Company.objects.get(pk=pk)
    print(company.tickets)
    content = {"company": company}
    templates = loader.get_template("product/companies.html")
    return HttpResponse(templates.render(content, request))
