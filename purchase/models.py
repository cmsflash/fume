from django.db import models
from member.models import Member
from games.models import Item

class PurchaseRecord(models.Model):

    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    
    @classmethod
    def create(cls, member, item):
        return cls(member=member, item=item)
