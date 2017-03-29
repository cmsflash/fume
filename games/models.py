from django.db import models

class Game(models.Model):
	ACTION = 'AC'
	ADVENTURE = 'AD'
	RACING = 'RA'
	RPG = 'RP'
	SIMULATION = 'SI'
	SPORTS = 'SP'
	STRATEGY = 'ST'
	GENRES = (
		(ACTION, 'Action'),
		(ADVENTURE, 'Adventure'),
		(RACING, 'Racing'),
		(RPG, 'RPG'),
		(SIMULATION, 'Simulation'),
		(SPORTS, 'Sports'),
		(STRATEGY, 'Strategy')
	)
	genre = models.CharField(max_length=2, choices=GENRES)
	title = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=100)
	detail = models.TextField()
	thumbnail = models.ImageField(upload_to='images/thumbnails')
	cover = models.ImageField(upload_to='images/covers')

	def __str__(self):
		return self.title


class Item(models.Model):
	LINUX = 'L'
	MACOS = 'M'
	WINDOWS = 'W'
	PLATFORMS = (
		(LINUX, 'Linux'),
		(MACOS, 'macOS'),
		(WINDOWS, 'Windows')
	)
	platform = models.CharField(max_length=1, choices=PLATFORMS)
	game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='items')
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.game.title + ' - ' + self.get_platform_display()

	class Meta:
		unique_together = ["game", "platform"]
