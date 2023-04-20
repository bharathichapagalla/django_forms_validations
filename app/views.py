from django.shortcuts import render

from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def chitti(request):
    TO=topics()
    d={'TO':TO}
    if request.method=='POST':
        TOD=topics(request.POST)
        if TOD.is_valid():

            topic_name=TOD.cleaned_data['topic_name']
            TO=topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TOD=topic.objects.all()

            return HttpResponse('topic_name is done successfully')

    return render(request,'topic_name.html',d)