from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
def home(request):
    items = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'items' : items,
        'name' : 'Sannan'
    }
    return render(request, 'food/index.html', context)

def item(request, item_id):
    return HttpResponse(f"The id of this item is {item_id}")