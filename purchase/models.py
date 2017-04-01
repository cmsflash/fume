from django.db import models
from member.models import Member
from games.models import Item

class PurchaseRecord(models.Model):

    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    game_object = models.ForeignKey(Item, on_delete = models.CASCADE)

    @classmethod
    def create(cls, member, game_product):
        return cls(member=member, game_product=game_product)
