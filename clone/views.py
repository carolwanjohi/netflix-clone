from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    '''
    View function for the home page when an authenticated user is logged in
    '''
    title = 'Home'
    message = 'I work'
    return render(request, 'all-posts/index.html', {"title": title, "message": message})
