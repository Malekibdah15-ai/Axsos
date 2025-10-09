from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context={
        'users' : users   
        }

    return render(request, 'index.html',context )

def users(request):
    print("hello")
    if request.method =='POST':
        print("hello2")
        first = request.POST['first']
        last =request.POST['last']
        name=first+" "+last 
        email = request.POST['email']
        age = request.POST['age']
        print(request.POST)
        User.objects.create(Name= name, Email= email, age= age)
        
    return redirect('/')
