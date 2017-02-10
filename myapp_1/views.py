from django.shortcuts import render
import datetime

# Create your views here.

def func(request):
    today = datetime.datetime.now()
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday',
                    'Saturday','Sunday']
    return render(request,'Tags.html',{'today':today,'dow':days_of_week})
