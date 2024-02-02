from django.shortcuts import render
from . import fulfill

def home(request):
    return render(request,'index.html')

def result(request):
    user_ask_value = request.GET["user_ask_inputbox"]
    ml_response = fulfill.model_response(user_ask_value)
    return render(request,'result.html',{'model_response':ml_response})