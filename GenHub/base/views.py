from django.shortcuts import render

rooms = [{"id":1, "name": "lets learn python"},
         {"id":1, "name": "ldesign with me"},
         {"id":1, "name": "frontend feveloper"},
         ]

def home(request):
    context = {"rooms":rooms}
    return render(request, "base/home.html", context)

def room(request):
    return render(request, "base/room.html")