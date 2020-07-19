from django.shortcuts import render
from .models import BlogModel

def homeView(request):
    return render(request, 'blogapp/home.html')

def listBlogsView(request):
    data = BlogModel.objects.all()
    context = {
        'data': data
    }
    return render(request, 'blogapp/list.html',context)