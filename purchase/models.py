from django.db import models
from member.models import Member
from games.models import Item

class PurchaseRecord(models.Model):

    member = models.ForeignKey(Member, on_delete = models.CASCADE, related_name='purchase_records')
    item = models.ForeignKey(Item, on_delete = models.CASCADE, related_name='purchase_records')
    
    @classmethod
    def create(cls, member, item):
        return cls(member=member, item=item)
