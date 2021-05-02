from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import redirect
from .models import Orders
from .forms import OrderForm


# Create your views here.

@require_POST
def create_order(request):
    """create a new order"""
    try:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders/')
    except ValueError as err:
        return JsonResponse({'Error': err})

@require_GET
def new_order(request):
    return render(request, 'create_order.html')

@require_GET
def order_detail(request, id):
    """Show a order details"""
    try:
        order= Orders.objects.get(id=id) # filter returns a query or .get returns an object
        order = order.serializer() #returns a dictionary
        return JsonResponse(order, status=200) # converts a dictionary in a json format
    except Exception:
        return HttpResponseNotFound('<h1>Error: order not found<h1>')
    

@require_GET
def status(request, id):
    """show order status"""
    order = Orders.objects.get(id=id)
    stat = order.status
    stat = stat.serialize()
    return JsonResponse(stat, status=200)

@require_GET
def list_orders(request):
    """Show all the orders"""
    return JsonResponse({'orders':
        [order.serializer() for order in Orders.objects.all()]
    })
