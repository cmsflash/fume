from django.db import models
from member.models import Member
from games.models import Game

class Tag(models.Model):

    label = models.TextField(max_length=100)

    @classmethod
    def create(cls, label):
        return cls(label=label)

class TagItem(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_items')
    tagger = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='tag_items')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='tag_items')

    @classmethod
    def create(cls, tag, tagger, game):
        return cls(tag=tag, tagger=tagger, game=game)
