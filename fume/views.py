from django.shortcuts import render
from member.models import Member
from recommendation.classes import Recommender

def index(request):
    if request.user.is_authenticated():
        member = request.user.member
        context = {'authenticated':True, 'recommendations':Recommender.make_recommendations(member)}
    else:
        context = {'authenticated':False}
    return render(request, 'fume/index.html', context)
