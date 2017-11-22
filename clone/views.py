from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    '''
    View function for the home page when an authenticated user is logged in
    '''
    title = 'Home'
    message = 'I work'
    return render(request, 'all-posts/index.html', {"title": title, "message": message})
