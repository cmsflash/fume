from django.db import models

# Create your models here.
class Game(models.Model):
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 1500)
	def __str__(self):
		return self.title

class GameProduct(models.Model):
	game = models.ForeignKey(Game, on_delete = models.CASCADE, related_name = 'product')
	platform = models.CharField(max_length = 10)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	def __str__(self):
		return self.game.title


class Image(models.Model):
	game = models.ForeignKey(Game, on_delete = models.CASCADE)
	small = models.CharField(max_length = 100)
	large = models.CharField(max_length = 100)
	def __str__(self):
		return self.game.title