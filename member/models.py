from django.db import models
from django.contrib.auth.models import User
import datetime

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
	nickname = models.CharField(max_length=100)
	avatar = models.ImageField(upload_to='images/avatars', default='images/avatars/default.jpg')
	accumulated_spending = models.IntegerField(default=0)

	@classmethod
	def create(cls, user, nickname):
		return cls.objects.create(user=user, nickname=nickname)

	def get_number_of_rewards(self):
		return self.rewards.filter(expiration_date__gte=datetime.datetime.now()).count()

	def get_rewards(self):
		return self.rewards.filter(expiration_date__gte=datetime.datetime.now()).order_by('expiration_date')

	def use_rewards(self, number):
		expiredRewards = self.rewards.filter(expiration_date__lt=datetime.datetime.now())
		usedRewards = self.rewards.filter(expiration_date__gte=datetime.datetime.now()).order_by('expiration_date')[:number]
		for reward in list(expiredRewards) + list(usedRewards):
			reward.delete()

	def accumulate_spending(self, amount):
		self.accumulated_spending += amount
		while self.accumulated_spending >= Reward.THRESHOLD:
			Reward.create(member=self, date=datetime.datetime.now() + datetime.timedelta(days=120))
			self.accumulated_spending -= Reward.THRESHOLD

	def get_purchase_history(self):
		return self.purchase_records

	def __str__(self):
		return self.nickname

class PaymentMethod(models.Model):
	account_number = models.IntegerField()
	member = models.OneToOneField(Member, on_delete = models.CASCADE, related_name='payment_method')

	@classmethod
	def create(cls, account_number, member):
		return cls.objects.create(account_number=account_number, member=member)

	def __str__(self):
		return self.member.nickname

class Reward(models.Model):

	THRESHOLD = 100

	expiration_date = models.DateTimeField()
	member = models.ForeignKey(Member, on_delete = models.CASCADE, related_name='rewards')
	@classmethod
	def create(cls, member, date):
		return cls.objects.create(member=member, expiration_date=date)

	def __str__(self):
		return self.member.nickname + ' ' + self.expiration_date.strftime("%Y-%m-%d %H:%M:%S")
