#-*- coding: utf-8 -*-

from django.shortcuts import render
#from module.models import model, model1
from sondages.models import Sondage, Response
from django.shortcuts import render_to_response


# Create your views here.

def homepage(request):
    list_sondages = Sondage.objects.all()
    
    return render_to_response('sondages/homepage.html',
                              {'list_sondages':list_sondages,
                               'page_title':'Acceuil des sondages',
                               'username':'Joel'})
    
