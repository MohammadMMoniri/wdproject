from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from cart.models import ShoppingCart, BookCountCart
from ticket.models import Ticket


@login_required
def shopping_cart_view(request):
    user_shopping_cart = ShoppingCart.objects.get(user=request.user)

    tickets_in_cart = BookCountCart.objects.filter(cart=user_shopping_cart)

    context = {"tickets_in_cart": tickets_in_cart}
    return render(request, "cart/shopping_cart.html", context)


def add_to_cart(request):
    if request.method == "POST":
        ticket_id = request.POST.get("ticket_id")
        ticket = get_object_or_404(Book, pk=ticket_id)

        shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
        ticket_count_cart, created = BookCountCart.objects.get_or_create(
            cart=shopping_cart, ticket=ticket
        )
        if not created:
            ticket_count_cart.count = ticket_count_cart.count + 1
        ticket_count_cart.save()

        return JsonResponse({"success": True})
    return JsonResponse({"success": False})


def remove_ticket(request):
    if request.method == "POST":
        ticket_id = request.POST.get("ticket_id")
        ticket = get_object_or_404(Book, pk=ticket_id)
        shopping_cart = get_object_or_404(ShoppingCart, user=request.user)
        ticket_count_cart = get_object_or_404(
            BookCountCart, cart=shopping_cart, ticket=ticket
        )
        if ticket_count_cart.count < 2:
            ticket_count_cart.delete()
        else:
            ticket_count_cart.count = ticket_count_cart.count - 1
            ticket_count_cart.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})
