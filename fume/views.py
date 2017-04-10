from django.shortcuts import render
from member.models import Member
from recommendation.classes import Recommender

def index(request):
    member = Member.objects.get(pk=1)
    context = {'recommendations':Recommender.make_recommendations(member)}
    return render(request, 'fume/index.html', context)
