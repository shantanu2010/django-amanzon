from django.shortcuts import render

def wanna_prime(request):

    return render(request, 'wannaprime/index.html',context=None)