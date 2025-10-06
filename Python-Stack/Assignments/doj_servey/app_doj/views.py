from django.shortcuts import render,HttpResponse, redirect

def index(request):
    return render(request,"index.html")


def creat_user(request):
    print("helloooooo")
    name = request.POST['name']
    location = request.POST['location']
    Language = request.POST['Language']
    comment = request.POST['comment']
    
    
    context= {
        "name" : name,
        "location" : location,
        "Language" : Language,
        "comment" : comment,
        
    }
    # Language = request.POST
    print(name)
    print (location)
    return render(request, 'index_one.html',context) #redirect /new


