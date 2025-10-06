from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if request.method == "get":
        print("snfvpojnpsinfvipnsripvbipyshbfinsjdnv0")
        return render(request, "some_template.html")
    if request.method == "post":
        print("bsibviygsivniusughf")
        return redirect("/")
    
def  some_function(requeust):
    if requeust.method == "post":
        val_from_field_one = requeust.post("one")
        val_from_field_tow = requeust.post("tow")
        