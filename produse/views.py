from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from produse.models import Products
from .forms import ProductsForm

# products = [
#     {
#         'id': 1,
#         'name': 'telefon',
#         'bought': True
#     },
#     {
#         'id': 2,
#         'name': 'laptop',
#         'bought': True
#     },
#     {
#         'id': 3,
#         'name': 'paine',
#         'bought': False
#     }
# ]


def home(request):
    # return HttpResponse("<h1>Aici este lista cu produse</h1>")
    if request.method == 'POST':
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            products = Products.objects.all()
            context = {'form':form, 'products': products}
            return render(request, 'produse/home.html',context)
    else:
        form = ProductsForm()
        products = Products.objects.all()
        context = {'form': form, 'products': products}
        return render(request, 'produse/home.html', context)


def delete(request, id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

def change_status(request, id):
    product = Products.objects.get(pk=id)
    if product.bought:
        product.bought = False
        product.save()
    else:
        product.bought = True
        product.save()
    return redirect('home')
def about(request):
    # return HttpResponse("<h2>About my app</h2>")
    return render(request, 'produse/about.html')






