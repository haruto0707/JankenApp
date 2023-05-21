from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupUserForm, LoginForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect(to='/janken/')
    else:
        form = SignupUserForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/janken/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def ranking_view(request):
    users = User.objects.order_by('-win_rate')
    return render(request, 'ranking.html', {'users': users})

@login_required
def logout_view(request):
    logout(request)

    return redirect(to='/janken/login')

@login_required
def index_view(request):
    return render(request, 'index.html', {'user': request.user})

@login_required
def user_view(request, id=0):
    other = get_object_or_404(User, id=id)
    params = {
        'user': request.user,
        'other': other
    }
    return render(request, 'user.html', params)

@login_required
def janken_view(request):
    if request.method == 'POST':
        com_hand = random.choice(('stone', 'scissors', 'paper'))
        player_hand = request.POST.get('hand')

        player = request.user

        result = player.play(player_hand, com_hand)
        player.save()

        params = {
            'user' : request.user,
            'result' : result,
            'player_hand' : player_hand,
            'com_hand' : com_hand
        }

        return render(request, 'result.html', params)
    else:
        return render(request, 'janken.html', {'user': request.user})

