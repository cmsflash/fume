from django.db import models

class Member(models.Model):

class GameProduct(models.Model):

class PurchaseRecord(models.Model):

    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    game_object = models.ForeighnKey(GameProduct, on_delete = models.CASCADE)

    def __init__(self, member, game_product):
        self.member = member
        self.game_object = game_product
