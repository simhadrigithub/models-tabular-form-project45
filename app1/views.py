from django.shortcuts import render

from app1.models import *

from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    tn=input('enter name : ')
    to=topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    return HttpResponse('inserting data successfully done')
def insert_webpage(request):
    tn=input('enter topic name: ')
    to=topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    wn=input('enter webpage name: ')
    u=input('enter url : ')
    wo=webpage.objects.get_or_create(Topic_name=to,name=wn,url=u)[0]
    wo.save()
    return HttpResponse('inserting data successfully done')

def insert_accessrecord(request):
    tn=input('enter topic name: ')
    to=topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    wn=input('enter webpage name: ')
    u=input('enter url : ')
    wo=webpage.objects.get_or_create(Topic_name=to,name=wn,url=u)[0]
    wo.save()
    d=input('enter date : ')
    a=input('enter author name : ')
    ao=accessrecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('inserting data successfully done')

