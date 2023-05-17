from django.shortcuts import render, HttpResponse
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
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

