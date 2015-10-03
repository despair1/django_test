from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"game/index.html",{"error_message1":"",
                                                 }) 
    return HttpResponse("you in index")

def test_json(request):
    j={"hello":"aaa","phaser":2}
    return JsonResponse(j)
    
    