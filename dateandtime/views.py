from django.shortcuts import render
from datetime import datetime
x = datetime.now
# Create your views here.
def input(request):
    return render(request, 'input.html',{'date' : x})
