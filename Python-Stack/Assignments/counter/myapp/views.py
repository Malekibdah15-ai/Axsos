from django.shortcuts import render, redirect

def index(request):
    if'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    return render(request, "index.html")
    
def destroy_session(request):
    request.session.flush()
    return redirect('/')

  