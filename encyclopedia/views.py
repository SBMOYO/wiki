from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from markdown2 import Markdown
import markdown

import re

from . import util


def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
      
    })


def get_title(request, title):
    content = convert_md_to_html(title)

    if content == None:
        content = markdown.markdown(f"## {title.capitalize()}\'s page has not been found")
   
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": content,
    })


def search(request):

    # check to see if request is post
    if request.method == "POST":

        # saving the data submitted by the user inside form
        search_word = request.POST['q']
        
        content = convert_md_to_html(search_word)

        # Initialize matching_files to an empty list
        matching_files = []
    
        if content == None:

            # intialize filenames to an empty list
            filenames = []
            
            dir_contents = default_storage.listdir("entries")
            for filename in dir_contents:
                filenames.append(filename)
            
            files = filenames[1]
            files = [file[:-3] for file in files]
            
            for file in files:
                search_word = search_word.lower()
                if search_word in file.lower():
                    matching_files.append(file)
            
            print(matching_files)
            content = None
        
        
        return render(request, "encyclopedia/search.html", {
            "title": search_word,
            "content": content,
            "entries": matching_files
        })
        