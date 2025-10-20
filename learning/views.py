from django.shortcuts import render




# Create your views here.
def index(request ):
    return render( request, 'learning/index.html')


def dashboard(request):
    return render( request, 'learning/dashboard.html')



def resources(request):
    return render( request, 'learning/resources.html')


def blog(request):
    return render( request, 'learning/blog.html')


def contact(request):
    return render( request, 'learning/contact.html')

def about(request):
    return render( request, 'learning/about.html')


def signup(request):
    return render( request, 'learning/signup.html')


def login(request):
    return render( request, 'learning/login.html')


def quiz(request):
    return render( request, 'learning/quiz.html')