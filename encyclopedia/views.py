from django.shortcuts import render, HttpResponse
from django import forms
import markdown

from . import util


class Search(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search encyclopedia...'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": Search()
    })


def get_title(request, title):
    content = util.get_entry(title)

    if content is None:
        content = markdown.markdown(f"## {title.capitalize()}\'s page has not been found")

    content = markdown.markdown(content)    
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": content
    })


def search(request):

    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q']

