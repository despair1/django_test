from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
@login_required
def index(request):
    print request.user.username,"uname"
    return render(request,"game/index.html",{"error_message1":"",
                                             'username':request.user.username,
                                                 }) 
    return HttpResponse("you in index")

def test_json(request):
    j={"hello":"aaa","phaser":2}
    return JsonResponse(j)

def recive_json(request):
    j={"max":50,
       "own":[
              [1,2,50],
              [2,3,15],
              [3,7,45]]}
    print "forbiden"
    #return HttpResponse("you in index")
    return JsonResponse(j)
def units_json(request):
    j={"max":50,
       "own":[
              [1,2,50],
              [2,3,15],
              [3,7,45]]}
    return JsonResponse(j)
    
    