from datetime import datetime

from django.core.mail import send_mail

from games.models import Item
from member.models import Member, PaymentMethod
from .models import PurchaseRecord


class Purchase:

    def __init__(self, member: Member, item: Item):
        self.member: Member = member
        self.item: Item = item
        self.price: float = float(item.get_price())
        self.number_of_rewards: int = 0

    def set_number_of_rewards(self, number_of_rewards: int) -> None:
        if number_of_rewards <= self.member.get_number_of_rewards():
            self.number_of_rewards = number_of_rewards
            self.price = (
                float(self.item.get_price()) * (1 - 0.1 * number_of_rewards))

    def get_amount(self) -> float:
        return self.price

    def make_payment(self) -> bool:
        payment = Payment(self.member.get_payment_method())
        successful = payment.pay(self.price)
        if successful:
            self.record_purchase()
            self.member.use_rewards(self.number_of_rewards)
            self.member.accumulate_spending(self.price)
            send_mail(
                'Receipt of your purchase on Fume',
                f'Dear {self.member.nickname},'
                f'\n\n'
                f'Thank you for purchasing on Fume.'
                f' You have purchased the game {self.item.game.title}.'
                f' This is your receipt.'
                f'\n\n'
                f'Best,'
                f'\n'
                f'Fume',
                'noreply@fume.com',
                [self.member.user.email],
                fail_silently=True,
            )
        return successful

    def record_purchase(self) -> None:
        record = PurchaseRecord.create(
            self.member, self.item, datetime.now(), self.number_of_rewards)
        record.save()


class Payment:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def pay(self, amount: float) -> bool:
        return True
