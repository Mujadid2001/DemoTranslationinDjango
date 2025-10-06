from django.shortcuts import render
from django.utils.translation import gettext as _

def home_view(request):
    greeting = _("Hello World")  # 👈 Marked for translation
    return render(request, "home/home.html", {"greeting": greeting})
