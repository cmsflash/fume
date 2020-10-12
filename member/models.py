from __future__ import annotations

import datetime
from typing import List, TYPE_CHECKING

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

if TYPE_CHECKING:
    from purchase.models import PurchaseRecord


class Member(models.Model):
    user: models.OneToOneField = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='member')
    nickname: models.CharField = models.CharField(max_length=100)
    avatar: models.ImageField = models.ImageField(
        upload_to='images/avatars', default='images/avatars/default.jpg')
    accumulated_spending: models.IntegerField = models.IntegerField(default=28)

    @classmethod
    def create(cls, user: User, nickname: str) -> Member:
        return cls.objects.create(user=user, nickname=nickname)

    def get_number_of_rewards(self) -> int:
        return self.rewards.filter(
            expiration_date__gte=datetime.datetime.now()).count()

    def get_payment_method(self) -> PaymentMethod:
        return self.payment_method

    def get_rewards(self) -> List['Reward']:
        return self.rewards.filter(
            expiration_date__gte=datetime.datetime.now()
        ).order_by('expiration_date')

    def use_rewards(self, number: int) -> None:
        expiredRewards = self.rewards.filter(
            expiration_date__lt=datetime.datetime.now())
        usedRewards = self.rewards.filter(
            expiration_date__gte=datetime.datetime.now()
        ).order_by('expiration_date')[:number]
        for reward in list(expiredRewards) + list(usedRewards):
            reward.delete()

    def accumulate_spending(self, amount: float) -> None:
        self.accumulated_spending = self.accumulated_spending + amount
        print(self.accumulated_spending)
        number_of_new_rewards = 0
        while self.accumulated_spending >= Reward.THRESHOLD:
            number_of_new_rewards += 1
            Reward.create(
                member=self,
                date=datetime.datetime.now() + datetime.timedelta(days=120),
            )
            self.accumulated_spending -= Reward.THRESHOLD
        if number_of_new_rewards > 0:
            send_mail(
                'New Rewards',
                f'You got {number_of_new_rewards} new rewards.',
                'noreply@fume.com',
                [self.user.email],
                fail_silently=True,
            )
        self.save()

    def get_purchase_history(self) -> List[PurchaseRecord]:
        return self.purchase_records

    def __str__(self) -> str:
        return self.nickname


class PaymentMethod(models.Model):
    account_number: models.IntegerField = models.IntegerField()
    member: models.OneToOneField = models.OneToOneField(
        Member, on_delete = models.CASCADE, related_name='payment_method')

    @classmethod
    def create(cls, account_number: int, member: Member) -> PaymentMethod:
        return cls.objects.create(account_number=account_number, member=member)

    def get_account(self) -> int:
        return self.account_number

    def __str__(self) -> str:
        return self.member.nickname


class Reward(models.Model):
    THRESHOLD: int = 100

    expiration_date: models.DateTimeField = models.DateTimeField()
    member: models.ForeignKey = models.ForeignKey(
        Member, on_delete = models.CASCADE, related_name='rewards')

    @classmethod
    def create(cls, member: Member, date: datetime.date) -> Reward:
        return cls.objects.create(member=member, expiration_date=date)

    def __str__(self) -> str:
        return (
            f'{self.member.nickname}'
            f' {self.expiration_date.strftime("%Y-%m-%d %H:%M:%S")}'
        )
