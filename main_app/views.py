from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Quote


# Create your views here.

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def quotes_index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', { 'quotes': quotes })

def category(request, quote_category):
    # category = list(Quote.objects.filter(category=quote_category).values())
    # category = Quote.objects.get(category=quote_category)
    # print(quote_category)
    # print(category)
    # print(type(category))
    quotes = Quote.objects.all()
    return render(request, 'category/index.html', { 'quote_category': quote_category, 'category': category, 'quotes': quotes })

def quotes_detail(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request, 'quotes/detail.html', { 'quote': quote })

class QuoteCreate(CreateView):
    model = Quote
    fields = '__all__'
    success_url = '/quotes/'

class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['quote', 'by']

class QuoteDelete(DeleteView):
    model = Quote
    success_url = '/quotes/'