from django.shortcuts import render

def home_page(request):
    context = {"home": True}
    return render(request, "home.html", context)
