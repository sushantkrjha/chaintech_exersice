from django.shortcuts import render
from .forms import UserForm
from .models import User


# Create your views here.
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return render(request, 'myapp/sucess.html')

    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form': form})
  