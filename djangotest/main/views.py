from django.shortcuts import render



def test(request):
    return render(request, 'main/greenword.html')

def about(request):
    return render(request, 'main/about.html')
def hope(request):
    return render(request, 'main/hope.html')