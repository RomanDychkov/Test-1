from django.shortcuts import render

def bd(request):
    return render(request, 'main/greenword.html')
