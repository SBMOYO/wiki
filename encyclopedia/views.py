from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from markdown2 import Markdown
import markdown
import random

import re

from . import util


class New_entry(forms.Form):
    title =  forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'style': 'height: 300px; display: block;'}))


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
            
            if not matching_files:
                content = markdown.markdown(f"## {search_word.capitalize()}\'s page has not been found")

        return render(request, "encyclopedia/search.html", {
            "title": search_word,
            "content": content,
            "entries": matching_files
        })


def new_page(request):

    if request.method == "POST":

        new_form = New_entry(request.POST)

        if new_form.is_valid():

            clean_form = new_form.cleaned_data
            title = clean_form["title"]
            content = clean_form["body"]

            if util.get_entry(title) is None:

                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("encyclopedia:get_title", args=[title]))
            
            else:
                # handle case where title already exists
                content = markdown.markdown(f"## {title.capitalize()}\'s page already exist")
                return render(request, "encyclopedia/error.html", {
                    "content": content
                })
                
    else:
        new_form = New_entry()
        return render(request, "encyclopedia/new_page.html", {
            "form": new_form
            })


def edit_page(request):

    if request.method == "POST":

        title = request.POST['entry_title']
        content = util.get_entry(title)

        initial_data = {'title': title, 'body': content}
        form = New_entry(initial=initial_data)

        return render(request, "encyclopedia/edit_page.html", {
            "form": form
        })
    

def save_edit(request):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['body']

        util.save_entry(title, content)
        #html_content = convert_md_to_html(title)

        return HttpResponseRedirect(reverse("encyclopedia:get_title", args=[title]))


def random_page(request):

    # intialize filenames to an empty list
    filenames = []
    
    dir_contents = default_storage.listdir("entries")
    for filename in dir_contents:
        filenames.append(filename)
    
    files = filenames[1]
    files = [file[:-3] for file in files]

    page = random.choice(files)

    return HttpResponseRedirect(reverse("encyclopedia:get_title", args=[page]))

