from django.shortcuts import render


# Create your views here.
def index(request):
    cont = {}
    return render(request, 'Login_app/index.html', context=cont)
