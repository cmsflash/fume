from datetime import datetime

from django.db import models

from member.models import Member
from games.models import Item


class PurchaseManager(models.Manager):

    def get_purchase_records_of(self, member):
        return list(self.filter(member=member).order_by('-date_time'))


class PurchaseRecord(models.Model):

    member = models.ForeignKey(
        Member, on_delete = models.CASCADE, related_name='purchase_records'
    )
    item = models.ForeignKey(
        Item, on_delete = models.CASCADE, related_name='purchase_records'
    )
    number_of_rewards_applied = models.IntegerField()
    date_time = models.DateTimeField()
    objects = PurchaseManager()
    
    @classmethod
    def create(cls, member, item, date_time, number_of_rewards_applied):
        return cls(
            member=member, item=item, date_time=date_time,
            number_of_rewards_applied=number_of_rewards_applied
        )
