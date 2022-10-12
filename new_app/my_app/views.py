from django.shortcuts import render
from django.http import HttpResponse


def mainView(request):
    code = '''
        <h1>Hello world</h1>
        <h1>My first deploying web-site</h1>
    '''
    return HttpResponse(code)