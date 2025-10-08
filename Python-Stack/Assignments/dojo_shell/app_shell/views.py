from django.shortcuts import render, HttpResponse, redirect
from . import models 

# Create your views here.
def index(request):
    
    context ={
        "dojos": models.get_all_dojos()
        }
    return render(request, 'index.html', context)

def create_Dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city=request.POST['city']
        state=request.POST['state']
        print(f'  {name} - {city} - {state} ')
        models.Dojos.objects.create( name = name, city=city, state= state)
    return redirect('/')

def create_ninja(request):
   
    if request.method == 'POST':
        dojo_id = request.POST['dojo']
        dojo = models.Dojos.objects.get(id=dojo_id)
        models.Ninjas.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            dojo = dojo
        )
    return redirect('/')
        
