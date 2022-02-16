from django.shortcuts import render
from .forms import BlogForm
import backend


def index(request):
    idea = []
    graphic = True
    if request.method == "POST":
        graphic = False
        form = BlogForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            keywords = form.cleaned_data['keywords']
            # idea = backend.ideaGenerator(category, keywords)
            idea = ["A", "B", "C", "D"]

    else:
        form = BlogForm()
    return render(request, 'home.html', {'form': form, 'idea': idea, 'graphic': graphic})
