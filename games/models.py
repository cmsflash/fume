import datetime

from django.db import models


class Game(models.Model):
	ACTION = 'AC'
	ADVENTURE = 'AD'
	RACING = 'RA'
	RPG = 'RP'
	SIMULATION = 'SI'
	SPORTS = 'SP'
	STRATEGY = 'ST'
	GALGAME = 'GG'
	GENRES = (
		(ACTION, 'Action'),
		(ADVENTURE, 'Adventure'),
		(RACING, 'Racing'),
		(RPG, 'RPG'),
		(SIMULATION, 'Simulation'),
		(SPORTS, 'Sports'),
		(STRATEGY, 'Strategy'),
		(GALGAME, 'GalGame')
	)
	genre = models.CharField(max_length=2, choices=GENRES)
	title = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=100)
	detail = models.TextField()
	thumbnail = models.ImageField(upload_to='images/thumbnails')
	cover = models.ImageField(upload_to='images/covers')
	date_published = models.DateField(default = datetime.datetime.now, blank = True)

	def __str__(self):
		return self.title

	def get_tags(self):
		return set([tagItems.tag for tagItems in self.tag_items.all()])

class Item(models.Model):
	LINUX = 'L'
	MACOS = 'M'
	WINDOWS = 'W'
	WINDOWSandMACOS = 'W&M'
	WINDOWSandLINUX = 'W&L'
	MACOSandLINUX = 'M&L'
	WINDOWSandMACOSandLINUX = 'W&M&L'
	PLATFORMS = (
		(LINUX, 'Linux'),
		(MACOS, 'macOS'),
		(WINDOWS, 'Windows'),
		(WINDOWSandMACOS, 'Windows & macOS'),
		(WINDOWSandLINUX, 'Windows & Linux'),
		(MACOSandLINUX, 'macOS & Linux'),
		(WINDOWSandMACOSandLINUX, 'Windows & macOS & Linux'),
		
	)
	platform = models.CharField(max_length=5, choices=PLATFORMS)
	game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='items')
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def get_price(self):
		return self.price

	def __str__(self):
		return self.game.title + ' - ' + self.get_platform_display()

	class Meta:
		unique_together = ["game", "platform"]

class FeaturedGame(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
