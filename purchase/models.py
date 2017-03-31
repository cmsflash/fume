from django.db import models
from member.models import Member
from games.models import GameProduct

class PurchaseRecord(models.Model):

    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    game_object = models.ForeignKey(GameProduct, on_delete = models.CASCADE)

    def __init__(self, member, game_product):
        self.member = member
        self.game_object = game_product
