from django.shortcuts import render

rooms = [{"id":1, "name": "lets learn python"},
         {"id":1, "name": "ldesign with me"},
         {"id":1, "name": "frontend feveloper"},
         ]

def home(request):
    return render(request, "home.html", {"rooms":rooms})

def room(request):
    return render(request, "room.html")