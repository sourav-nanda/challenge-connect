from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

# Define other views for other API endpoints in a similar manner...
