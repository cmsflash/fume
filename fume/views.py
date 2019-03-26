from django.shortcuts import render
from member.models import Member
from games.models import FeaturedGame
from recommendation.classes import Recommender

def index(request):
    featured_games = [featured_game.game for featured_game in FeaturedGame.objects.all()]
    if request.user.is_authenticated:
        member = request.user.member
        context = {'recommendations':Recommender.make_recommendations(member), 'featured_games': featured_games, 'spending_needed': 100 - member.accumulated_spending}
    else:
        context = {'authenticated':False, 'featured_games': featured_games}
    return render(request, 'fume/index.html', context)
