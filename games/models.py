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

    def get_game_products(self):
        return GameProduct.objects.filter(game=self)

    def __str__(self):
        return self.title


class GameProduct(models.Model):
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

class Member(models.Model):

    def __init__(self, username, password, nickname, email):
        pass

class PurchaseRecord(models.Model):

    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    game_product = models.ForeignKey(GameProduct, on_delete = models.CASCADE)

    def __init__(self, member, game_product):
        self.member = member
        self.game_product = game_product

class Tag(models.Model):

    text = models.CharField(max_length = 30)

    def __init__(self, text):
        self.text = text

    def get_games(self):
        tag_items = TagItem.objects.filter(tag=self)
        games = set()
        for tag_item in tag_items:
            games.add(tag_item.game)
        return list(games)

class TagItem(models.Model):
    
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    game = models.ForeignKey(GameProduct, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)

    def __init__(self, member, game, tag):
        self.member = member
        self.game = game
        self.tag = tag
