from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Quote:
    def __init__(self, quote, by):
        self.quote = quote
        self.by = by

quotes = [
    Quote("Life is a dream and I dream lucid", "J. Cole"),
    Quote("I'm nice at ping pong", "Kanye West"),
    Quote("Rest at the end, not the middle", "Kobe Bryant")

]

def home(request):
    return HttpResponse('<h1>Collector Home</h1>')

def about(request):
    return render(request, 'about.html')

def quotes_index(request):
    return render(request, 'quotes/index.html', { 'quotes': quotes })

