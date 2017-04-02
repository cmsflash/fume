from django.shortcuts import render, redirect
from .models import TagItem, Tag
from django.http import HttpResponse
from games.models import Game
from member.models import Member

def tag(request, game_id):
    game = Game.objects.get(pk=game_id)
    member = Member.objects.get(pk=1)
    tag_items = game.tag_items.all()
    tags = set()
    for tag_item in tag_items:
        tags.add(tag_item.tag)
    context = {'member':member, 'game':game, 'tags':tags}
    return render(request, 'tags/tag.html', context)

def add(request, game_id):
    game = Game.objects.get(pk=game_id)
    member = Member.objects.get(pk=1)
    label = request.GET.get('tag')
    tag = Tag.objects.get_or_create(label=label)[0]
    tag_item = TagItem.create(tag, member, game)
    tag_item.save()
    return redirect('games:game', gameID=game_id)