from django.shortcuts import render
from datetime import datetime
from home.models import Speaker

# Create your views here.
def index(request):
    obj = Speaker.objects.all()
    spe = {
        'object':obj
    }
    print(object)
    return render(request, 'index.html', spe)

def addSpeaker(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        speaker = Speaker(name=name, email=email, phone=phone, about=about, date=datetime.now())
        speaker.save()
        return render(request, "tick.html")
    return render(request, "addSpeaker.html")