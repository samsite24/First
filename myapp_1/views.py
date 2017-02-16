from django.shortcuts import render
import datetime
from .models import issue

# Create your views here.

def func(request):
    today = datetime.datetime.now()
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday',
                    'Saturday','Sunday']
    issues = issue.objects.order_by('-name')
    return render(request,'Tags.html',{'today':today,'dow':days_of_week,
                                       'issues':issues})
