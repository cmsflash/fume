import datetime
from typing import List, Set, Tuple

from django.db import models


class Game(models.Model):
	ACTION: str = 'AC'
	ADVENTURE: str = 'AD'
	RACING: str = 'RA'
	RPG: str = 'RP'
	SIMULATION: str = 'SI'
	SPORTS: str = 'SP'
	STRATEGY: str = 'ST'
	GALGAME: str = 'GG'
	GENRES: Tuple[Tuple[str, str], ...] = (
		(ACTION, 'Action'),
		(ADVENTURE, 'Adventure'),
		(RACING, 'Racing'),
		(RPG, 'RPG'),
		(SIMULATION, 'Simulation'),
		(SPORTS, 'Sports'),
		(STRATEGY, 'Strategy'),
		(GALGAME, 'GalGame'),
	)
	genre: models.CharField = models.CharField(max_length=2, choices=GENRES)
	title: models.CharField = models.CharField(max_length=100, unique=True)
	description: models.CharField = models.CharField(max_length=100)
	detail: models.TextField = models.TextField()
	thumbnail: models.ImageField = models.ImageField(
		upload_to='images/thumbnails')
	cover: models.ImageField = models.ImageField(upload_to='images/covers')
	date_published: models.DateField = models.DateField(
		default=datetime.datetime.now, blank=True)

	def __str__(self) -> str:
		return self.title

	def get_tags(self) -> Set:
		return set([tagItems.tag for tagItems in self.tag_items.all()])


class Item(models.Model):
	LINUX: str = 'L'
	MACOS: str = 'M'
	WINDOWS: str = 'W'
	WINDOWSandMACOS: str = 'W&M'
	WINDOWSandLINUX: str = 'W&L'
	MACOSandLINUX: str = 'M&L'
	WINDOWSandMACOSandLINUX: str = 'W&M&L'
	PLATFORMS: Tuple[Tuple[str, str], ...] = (
		(LINUX, 'Linux'),
		(MACOS, 'macOS'),
		(WINDOWS, 'Windows'),
		(WINDOWSandMACOS, 'Windows & macOS'),
		(WINDOWSandLINUX, 'Windows & Linux'),
		(MACOSandLINUX, 'macOS & Linux'),
		(WINDOWSandMACOSandLINUX, 'Windows & macOS & Linux'),
	)
	platform: models.CharField = models.CharField(
		max_length=5, choices=PLATFORMS)
	game: models.ForeignKey = models.ForeignKey(
		Game, on_delete=models.CASCADE, related_name='items')
	price: models.DecimalField = models.DecimalField(
		max_digits=10, decimal_places=2)

	def get_price(self) -> float:
		return self.price

	def __str__(self) -> str:
		return self.game.title + ' - ' + self.get_platform_display()

	class Meta:
		unique_together: List[str] = ["game", "platform"]


class FeaturedGame(models.Model):
	game: models.ForeignKey = models.ForeignKey(Game, on_delete=models.CASCADE)
