


from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return render(request, 'myapp/success.html')

    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form': form})
  


def user_data(request):
    users = User.objects.all()
    return render(request, 'myapp/user_data.html', {'users': users})



