from django.shortcuts import render,HttpResponse
from urllib.parse import unquote
# Create your views here.

def main_page(request):
    name = unquote(request.GET.get('name', 'None'))
    message = unquote(request.GET.get('message', 'None'))
    return render(request, 'main_rekruto/index.html', {'name':name, 'message': message})