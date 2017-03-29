from django.db import models
from datetime import datetime

class Member(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30)
	email = models.CharField(max_length=100)
	total_amount = models.CharField(max_length=100)
	paymentMethod = models.ForeignKey(PaymentMethod, on_delete = models.CASCADE)
	
	def get_rewards(self):
		rewards = Reward.objects.filter(member=self)
		now = time.time()
		for reward in rewards:
			if reward.expiration_date < now
				Reward.objects.get(expiration_date=reward.expiration_date, member=self).delete()
		return len(rewards)

	def use_rewards(number):
		rewards = Reward.objects.filter(member=self)
		now = datetime.now()
		for reward in rewards:
			if reward.expiration_date < now
				Reward.objects.get(expiration_date=reward.expiration_date, member=self).delete()
		sort(rewards, key=lambda reward: reward.expiration_date)
		for reward in range(number):
			Reward.objects.get(expiration_date=reward.expiration_date,member=self).delete()
	
	def accumulate_spending(amount):
		total_amount = total_amount+amount
		if total_amount>100:
			now = datetime.now()
			new_reward = Reward(now)
			new_reward.save()



		
class PaymentMethod(models.Model):
	account_number = models.CharField(max_length=50)

class Reward(models.Model):
	expiration_date = models.CharField(max_length=100)
	member = models.ForeignKey(Member, on_delete = models.CASCADE)
	def __init__(self,date):
		self.expiration_date = date


class PurchaseRecord(models.Model):

	member = models.ForeignKey(Member, on_delete = models.CASCADE)
	game_object = models.ForeighnKey(GameProduct, on_delete = models.CASCADE)

	def __init__(self, member, game_product):
		self.member = member
		self.game_object = game_product