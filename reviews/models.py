from __future__ import annotations

from datetime import date
from typing import List

from django.db import models

from games.models import Game
from member.models import Member


class ReviewManager(models.Manager):

    def get_reviews_of_game(self, game: Game) -> List[Review]:
        review_list = Review.objects.filter(game=game).order_by(
            '-date_published')
        return review_list


class Review(models.Model):
    content: models.TextField = models.TextField(max_length = 1000)
    game: models.ForeignKey = models.ForeignKey(
        Game, on_delete = models.CASCADE, related_name='game_of_review')
    reviewer: models.ForeignKey = models.ForeignKey(
        Member, on_delete = models.CASCADE, related_name='reviewer_of_review')
    date_published: models.DateField = models.DateField()
    objects: ReviewManager = ReviewManager()

    @classmethod
    def create(cls, content: str, game: Game, reviewer: Member) -> Review:
        return cls(
            content=content, game=game, reviewer=reviewer,
            date_published=date.today())
