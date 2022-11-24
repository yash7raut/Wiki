from django.shortcuts import HttpResponseRedirect, redirect, render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "entries": util.get_entry(title)
    })

def search(request):
    if request.method == "POST":
        searched = request.POST.get("q", "")
        result_list = []
        if util.get_entry(searched):
            return wiki(request,searched)
        else:
            for x in util.list_entries():
                if searched.lower() == x[:len(searched)].lower():
                    result_list.append(x)

    return render(request, "encyclopedia/search.html",{
        "result_list": result_list
    })