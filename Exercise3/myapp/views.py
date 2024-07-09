from django.shortcuts import render
from .utls import get_current_datetime, get_random_quote

# Create your views here.
def home(request):
    current_datetime = get_current_datetime()
    random_quote = get_random_quote()
    context = {
        'current_datetime': current_datetime,
        'random_quote': random_quote,
    }
    return render(request, 'myapp/index.html', context)
