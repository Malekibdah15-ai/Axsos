from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create_users(request):
    name = request.post['name']
    location = request.post['location']
    Language = request.post['language ']
    comment = request.post['comment']
    
    context = {
        "name" : name,
        "location" : location,
        "Language" : Language,
        "comment" : comment,
    }
    return render(request, 'login.html', context)



    