from django.shortcuts import render, redirect
from app_users.forms import ExtRegiserForm, EditBalForm
from app_users.models import Profile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.views import View



def register_view(request):
    if request.method == 'POST':
        form = ExtRegiserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/users/account')
    else:
        form = ExtRegiserForm()
    return render(request, 'reg.html', {'form': form})

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LogoutView):
    next_page = '/users/login'

def accuont_view(request):
    
    return render(request, 'account.html')

def edit_bal_view(request):
    if request.method == 'POST':
        form = EditBalForm(request.POST)
        if form.is_valid():
            old_bal = Profile.objects.get(user_id=request.user.id).balance
            Profile.objects.filter(user_id=request.user.id).update(balance=old_bal+form.cleaned_data['balance'])
            
            return redirect('/users/account')
    else:
        form = EditBalForm()
    return render(request, 'edit_balance.html', {'form': form})