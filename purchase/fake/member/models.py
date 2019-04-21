from datetime import date

from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    total_amount = models.FloatField()

    @classmethod
    def create(cls, username, password, nickname, email, payment_method):
        member = cls(
            username=username, password=password, nickname=nickname,
            email=email, total_amount=0, paymentMethod = payment_method
        )
        return member
        
    def get_rewards(self):
        rewards = Reward.objects.filter(member=self)
        for reward in rewards:
            if reward.expiration_date < date.today():
                Reward.objects.get(
                    expiration_date=reward.expiration_date, member=self
                ).delete()
        return len(rewards)

    def use_rewards(self, number):
        rewards = self.rewards.all()
        for reward in rewards:
            if reward.expiration_date < date.today():
                reward.delete()
        used_rewards = rewards.order_by('expiration_date')[:number]
        for reward in used_rewards:
            reward.delete()
    
    def accumulate_spending(self, amount):
        self.total_amount += amount
        while self.total_amount > Reward.THRESHOLD:
            new_reward = Reward.create(self, date.today())
            new_reward.save()
            self.total_amount -= Reward.THRESHOLD
        self.save()


class PaymentMethod(models.Model):
    account_number = models.IntegerField()
    member = models.OneToOneField(
        Member, on_delete = models.CASCADE, related_name='payment_method'
    )

    @classmethod
    def create(cls, account_number, member):
        return cls(account_number=account_number, member=member)


class Reward(models.Model):
    THRESHOLD = 100
    
    expiration_date = models.DateField()
    member = models.ForeignKey(
        Member, on_delete = models.CASCADE, related_name='rewards'
    )
    
    @classmethod
    def create(cls, member, date):
        return cls(expiration_date = date, member=member)
