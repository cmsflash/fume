from .models import PurchaseRecord
from datetime import datetime
from django.core.mail import send_mail

class Purchase:

    def __init__(self, member, item):
        self.member = member
        self.item = item
        self.price = float(item.get_price())
        self.number_of_rewards = 0

    def set_number_of_rewards(self, number_of_rewards):
        if number_of_rewards <= self.member.get_number_of_rewards():
            self.number_of_rewards = number_of_rewards
            self.price = float(self.item.get_price()) * (1 - 0.1 * number_of_rewards)

    def get_amount(self):
        return self.price

    def make_payment(self):
        payment = Payment(self.member.get_payment_method().get_account());
        successful = payment.pay(self.price)
        if successful:
            self.record_purchase()
            self.member.use_rewards(self.number_of_rewards)
            self.member.accumulate_spending(self.price)
            send_mail('Receipt of your purchase on Fume',
                      'Dear ' + self.member.nickname + ',\n\n'
                      + 'Thank you for purchasing on Fume. You have purchased the game '
                      + self.item.game.title + '.' + 'This is your receipt.\n\n'
                      + 'Best,\nFume',
                      'noreply@fume.com',
                      [self.member.user.email])
        return successful

    def record_purchase(self):
        record = PurchaseRecord.create(self.member, self.item, datetime.now(), self.number_of_rewards)
        record.save()

class Payment:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def pay(self, amount):
        return True
