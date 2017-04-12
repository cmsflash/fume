from django.db import models
from django.contrib.auth.models import User
import datetime

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
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
		self.rewards.filter(expiration_date__lt=datetime.datetime.now()).delete()
		self.rewards.filter(expiration_date__gte=datetime.datetime.now()).order_by('expiration_date')[:number].delete()

	def accumulate_spending(self, amount):
		self.accumulated_spending += amount
		if self.accumulated_spending >= Reward.THRESHOLD:
			Reward.create(member=self, date=datetime.datetime.now() + datetime.timedelta(days=120))
			self.accumulated_spending -= Reward.THRESHOLD

	def get_purchase_history(self):
		return self.purchase_records

class PaymentMethod(models.Model):
	account_number = models.IntegerField()
	member = models.OneToOneField(Member, on_delete = models.CASCADE, related_name='payment_method')

	@classmethod
	def create(cls, account_number, member):
		return cls.objects.create(account_number=account_number, member=member)

class Reward(models.Model):

	THRESHOLD = 100

	expiration_date = models.DateTimeField()
	member = models.ForeignKey(Member, on_delete = models.CASCADE, related_name='rewards')
	@classmethod
	def create(cls, member, date):
		return cls.objects.create(member=member, expiration_date=date)
