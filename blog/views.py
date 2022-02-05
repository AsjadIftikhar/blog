from django.shortcuts import render
from .forms import BlogForm


def index(request):
    idea = ""
    graphic = ""
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            keywords = form.cleaned_data['keywords']

            print(category)
            print(keywords)
            graphic = "none"
            idea = "Pets are great"
    else:
        graphic = "block"
        form = BlogForm()
    return render(request, 'home.html', {'form': form, 'idea': idea, 'graphic': graphic})
