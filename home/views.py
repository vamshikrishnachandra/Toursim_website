from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def favourite_places_view(request):
    return render(request, 'favourite_places.html')

def taj_mahal(request):
    return render(request, 'taj_mahal.html')

def golden_temple(request):
    return render(request, 'golden_temple.html')

def mysore_palace(request):
    return render(request, 'mysore_palace.html')

def varasani_temple(request):
    return render(request, 'varasani_temple.html')
