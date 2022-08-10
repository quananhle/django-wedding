from django.shortcuts import render

def index(request):
    template = 'index.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)