from django.shortcuts import render

from .models import Game, Member

default_member = Member('Qomo Inc', 'samson', 'Qomo', 'we@qomo.com')

def game(request, gameID):
	game = Game.objects.get(pk=gameID)
	detail_page = DetailPage(default_member, game)
	items = game.items.all()
	context = {'game': game, 'items': items}
	return render(request, 'games/game.html', context)

def genres(request):
	genres = [choice[1].lower() for choice in Game._meta.get_field('genre').choices]
	context = {'genres': genres}
	return render(request, 'games/genres.html', context)

def genre(request, genre):
	games = Game.objects.filter(genre=genre[:2].upper())
	context = {'genre': genre, 'games': games}
	return render(request, 'games/genre.html', context)
