

from random import randint

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from markdown import markdown

from . import util
from .forms import CreateEntry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "title": "All Pages",
        "entry": util.list_entries()
    })

def entry_view(request, title):

    entry = util.get_entry(title)

    if entry:
        entry_converted = markdown(entry)
    else:
        entry_converted = title



    if entry == None:
        return render(request, 'encyclopedia/page_not_found.html', {
            'title': title
        })

    return render(request, 'encyclopedia/entry.html', {
        'title': title,
        'entry': entry_converted
    })

def search(request):

    if not request.POST:
        return redirect(reverse('encyclopedia:index'))
    

    search_term = request.POST["q"].upper()
    entries = util.list_entries()



    results = []
    for entry in entries:
        if search_term == entry.upper():
            return redirect(f'/wiki/{search_term}')
        if search_term in entry.upper():
            results.append(entry)
        
    if len(results) == 0:
        return redirect(f'/wiki/{search_term.capitalize()}')
        
    if len(results) >= 1:
        return render(request, "encyclopedia/index.html", {
            "title": "Search results",
            "search_term": search_term.capitalize(),
            "entry": results
        })
    
def create_view(request):

    if request.POST:
        form = CreateEntry(request.POST)

    form = CreateEntry()

    return render(request, 'encyclopedia/create_entry.html', {
        'form': form
    })
    

def create_entry(request):

    if not request.POST:
        redirect(reverse('encyclopedia:create'))
    
    form = CreateEntry(request.POST)
    
    title = request.POST["title"]
    content = request.POST["content"]


    entries = util.list_entries()

    if form.is_valid():

        for entry in entries:
            if title.upper() == entry.upper():
                messages.error(request, 'An entry with that title already exists')
                return redirect(reverse('encyclopedia:create'))
                

        util.save_entry(title, content)

    
    return redirect(f'/wiki/{title}')

def edit_view(request, title):

    data = {
        'title': title,
        'content': f'{util.get_entry(title)}'
    } 

    form = CreateEntry(data)

    return render(request, 'encyclopedia/edit.html', {
        'form': form
    })        

def edit_entry(request):

    title = request.POST["title"]
    content = request.POST["content"]

    util.save_entry(title, content)

    return redirect(f'/wiki/{title}')


def random(request):

    entries = util.list_entries()

    random_entry = util.choice(entries)

    return redirect(f'/wiki/{random_entry}')


        

        
    



    
    


