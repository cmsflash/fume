from django.db import models
from member.models import Member
from games.models import Game
from datetime import date
# Create your models here.
class ReviewManager(models.Manager):

    def get_reviews_of_game(self, game):
        review_list = Review.objects.filter(game=game).order_by('-date_published')
        return review_list

class Review(models.Model):
    content = models.TextField(max_length = 1000)
    game = models.ForeignKey(Game, on_delete = models.CASCADE, related_name = 'game_of_review')
    reviewer = models.ForeignKey(Member, on_delete = models.CASCADE, related_name = 'reviewer_of_review')
    date_published = models.DateField()
    objects = ReviewManager()
    @classmethod
    def create(cls, content, game, reviewer):
        return cls(content=content, game=game, reviewer=reviewer, date_published=date.today())

