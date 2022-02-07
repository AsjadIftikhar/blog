from django.shortcuts import render
from .forms import BlogForm


def index(request):
    idea = ""
    graphic = True
    if request.method == "POST":
        graphic = False
        form = BlogForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']

            idea = "Pets are great"
    else:
        form = BlogForm()
    return render(request, 'home.html', {'form': form, 'idea': idea, 'graphic': graphic})
