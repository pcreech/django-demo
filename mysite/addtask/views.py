from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add as addtask
from .models import AddRequest
import time
# Create your views here.

def index(request):
    return HttpResponse("Hello, world?")

def add(request, left=0, right=0):
    req = AddRequest()
    req.left = int(left)
    req.right = int(right)
    req.save()
    result = addtask.delay(req.left, req.right)
    while not result.ready():
       time.sleep(1)
    req.total = result.get(timeout=20)
    req.save()
    output = "{} + {} = {}\n".format(req.left, req.right, req.total)
    return HttpResponse(output)
