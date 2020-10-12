from __future__ import annotations

from typing import List

from django.db import models

from games.models import Game
from member.models import Member


class TagManager(models.Manager):

	def get_tags_of_game(
		self, game: Game, order: str = 'Arbitrary'
	) -> List[TagItem]:
		tag_items = TagItem.objects.filter(game=game)
		tags = set()
		for tag_item in tag_items:
			tags.add(tag_item.tag)
		tags = list(tags)
		if (order == 'Lexicographical'):
			tags.sort(key=lambda tag: tag.label)
		return tags

	def get_games_by_tag(
		self, tag: 'Tag', order: str = 'Arbitrary'
	) -> List[Game]:
		tag_items = TagItem.objects.filter(tag=tag)
		games = set()
		for tag_item in tag_items:
			games.add(tag_item.game)
		games = list(games)
		return games

class Tag(models.Model):
	label: models.TextField = models.TextField(max_length=100)
	objects: TagManager = TagManager()

	@classmethod
	def create(cls, label: str) -> Tag:
		return cls(label=label)


class TagItem(models.Model):
	tag: models.ForeignKey = models.ForeignKey(Tag, on_delete=models.CASCADE)
	tagger: models.ForeignKey = models.ForeignKey(
		Member, on_delete=models.CASCADE)
	game: models.ForeignKey = models.ForeignKey(
		Game, on_delete=models.CASCADE, related_name='tag_items')

	@classmethod
	def create(cls, tag: Tag, tagger: Member, game: Game) -> TagItem:
		return cls(tag=tag, tagger=tagger, game=game)

