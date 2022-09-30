from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP
from django.views import View

class Home(View):
    template = 'home.html'
    def get(self, *args, **kwargs):
        context={
            'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
            'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
            'website_url': settings.WEDDING_WEBSITE_URL,
            'couple_name': settings.BRIDE_AND_GROOM,
            'wedding_location': settings.WEDDING_LOCATION,
            'wedding_date': settings.WEDDING_DATE,
        }
        return render(self.request, self.template, context)

def hanoi(request):
    template = 'hanoi.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)

def cantho(request):
    template = 'cantho.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)

def cantho(request):
    template = 'cantho.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)        

def engagement(request):
    template = 'partials/engagement.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)

def wedding(request):
    template = 'partials/wedding-party.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)

def save_the_date(request):
    template = 'partials/misc.html'
    if request.method == 'GET':
        context = {}
        return render(request, template, context)
