# Blog Views
from django.shortcuts import render

# Homepage
def index(request):
    return render(request, 'index.html', {})