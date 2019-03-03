from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

def recieve_form(request):
    return render_to_response('form_sender/main_form.html')

def response(request):
    print(request.GET['answer'])
    return render_to_response('form_sender/response.html')


