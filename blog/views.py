from django.shortcuts import render


def index(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render(request, 'home.html', {})