from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'policy/index.html')

def selah(request):
    return render(request, 'policy/selah.html')