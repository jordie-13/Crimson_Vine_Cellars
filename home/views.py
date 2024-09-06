from django.shortcuts import render

# Create your views here.
def home(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')


def about_us(request):
    """ A view to return the about us page """
    
    return render(request, 'about_us.html')
