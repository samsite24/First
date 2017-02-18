from django.shortcuts import render, get_object_or_404
import datetime
from .models import issue

# Create your views here.

issues = issue.objects.order_by('-name')

def func(request):
    today = datetime.datetime.now()
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday',
                    'Saturday','Sunday']
    return render(request,'Tags.html',{'today':today,'dow':days_of_week,
                                       'issues':issues})

def problems(request,pk):
    post = get_object_or_404(issue,pk=pk)
    return render(request,'problems.html',{'prob':post,'issues':issues})
