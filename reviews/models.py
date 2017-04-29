from django.db import models
from member.models import Member
from games.models import Game
# Create your models here.
class ReviewManager(models.Manager):
	def get_reviews_of_game(self, game, order='Arbitrary'):
		review_list = Review.objects.filter(game = game)
        #review_list = Review.objects.all()
		#reviews = set()
		#for review in review_list:
			#reviews.add((review.reviewer.nickname, review.content))
		#reviews = list(reviews)
		return review_list.reverse()
class Review(models.Model):
	content = models.TextField(max_length = 1000)
	game = models.ForeignKey(Game, on_delete = models.CASCADE, related_name = 'game_of_review')
	reviewer = models.ForeignKey(Member, on_delete = models.CASCADE, related_name = 'reviewer_of_review')
	objects = ReviewManager()
	@classmethod
	def create(cls, content, game, reviewer):
		return cls(content = content, game = game, reviewer = reviewer)

