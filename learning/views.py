from django.shortcuts import render




# Create your views here.
def index(request ):
    return render( request, 'learning/index.html')



def sidebar(request):
    return render( request, 'learning/sidebar.html')