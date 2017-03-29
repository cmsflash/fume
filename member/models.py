from django.db import models
from datetime import date

class Member(models.Model):
        
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete = models.CASCADE)

    def __init__(self, username, password, nickname, email):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.email = email
        self.total_amount = 0
        
    def get_rewards(self):
        rewards = Reward.objects.filter(member=self)
        for reward in rewards:
            if reward.expiration_date < date.today()
                Reward.objects.get(expiration_date=reward.expiration_date, member=self).delete()
        return len(rewards)

    def use_rewards(number):
        rewards = Reward.objects.filter(member=self)
        for reward in rewards:
            if reward.expiration_date < date.today()
                Reward.objects.get(expiration_date=reward.expiration_date, member=self).delete()
        sort(rewards, key=lambda reward: reward.expiration_date)
        for reward in rewards[0:number]:
            Reward.objects.get(expiration_date=reward.expiration_date, member=self).delete()
    
    def accumulate_spending(amount):
        total_amount = total_amount+amount
        if total_amount>100:
            new_reward = Reward(date.today())
            new_reward.save()



        
class PaymentMethod(models.Model):

    account_number = models.IntegerField()

    def __init__(self, account_number):
        self.account_number = account_number

class Reward(models.Model):
    expiration_date = models.DateTimeField()
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    def __init__(self,date):
        self.expiration_date = date
