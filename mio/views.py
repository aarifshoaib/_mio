from django.http import HttpResponse

# Home view definition
def home(request):
    return HttpResponse("Welcome to the Mio homepage!")