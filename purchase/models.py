from __future__ import annotations

from datetime import datetime
from typing import List

from django.db import models

from games.models import Item
from member.models import Member


class PurchaseManager(models.Manager):

    def get_purchase_records_of(self, member: Member) -> List[PurchaseRecord]:
        return list(self.filter(member=member).order_by('-date_time'))


class PurchaseRecord(models.Model):

    member: models.ForeignKey = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='purchase_records')
    item: models.ForeignKey = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='purchase_records')
    number_of_rewards_applied: models.IntegerField = models.IntegerField()
    date_time: models.DateTimeField = models.DateTimeField()
    objects: PurchaseManager = PurchaseManager()
    
    @classmethod
    def create(
        cls,
        member: Member,
        item: Item,
        date_time: datetime,
        number_of_rewards_applied: int,
    ) -> PurchaseRecord:
        return cls(
            member=member, item=item, date_time=date_time,
            number_of_rewards_applied=number_of_rewards_applied)
