from django.shortcuts import render

def index(request):
    return render(request, 'blog/blog_list.html')
