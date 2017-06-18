from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>In the Music Page</h1>")
