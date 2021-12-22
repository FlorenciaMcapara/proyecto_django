from django.shortcuts import render

# Create your views here.

def noticia_list(request):

    return render(request, 'blog/noticia_list.html', {})