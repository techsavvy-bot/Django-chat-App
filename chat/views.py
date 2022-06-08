from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # return render(request, "index.html", {})
    return redirect('/chat/login')


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/chat/createRoom')
        else:
            return render(request, "login.html")
    context = {}

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('/chat/login')

@login_required(login_url='/chat/login')
def createRoom(request):

    if request.method == "POST":
        create = request.POST.get('createroom')
        if request.user.is_authenticated:
            if create != "":
                return redirect(f'/chat/{create}')
            else:
                join = request.POST.get('join')
                return redirect(f'/chat/{join}')
    return render(request, "createRoom.html")


def signup(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, "signup.html", context)

@login_required(login_url='/chat/login')
def room(request, room_name):

    
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })
