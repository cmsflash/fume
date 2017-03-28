from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Game
from .models import GameProduct

def index(request):
	all_games = Game.objects.all()
	list = []
	for game in all_games:
		html = '<h1><a href = "/game/{id}">{title}</a></h1></br>'
		list.append(html.format(title = game.title, id = game.id))
	output = list
	return HttpResponse(output)

def viewGameDetails(request, game_id):
	game = Game.objects.get(pk=game_id)
	gameProducts = game.product.all()
	platforms = []
	for gameproduct in gameProducts:
		platforms.append(gameproduct.platform)
	
	html = """<h1>{title}</h1>
			<p>Drscription: {description}</p>
			<p>Platforms: {platform}</p>
			"""
	output = html.format(title = game.title, platform = platforms, description = game.description)
	return HttpResponse(output)