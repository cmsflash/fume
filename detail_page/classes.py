from .models import PaymentRecord

class detail_page:

    def __init__(self, member, game):
        self.member = member
        self.game = game

    def start_purchase(platform):
        game_product = self.game.get_game_product(platform)
        purchase = Purchase(member, game_product)
        return purchase

class Purchase:

    def __init__(self, member, game_product):
        self.member = member
        self.game_product = game_product
        self.price = game_product.get_price()

    def update_price(number_of_rewards):
        if number_of_rewards <= self.member.get_number_of_rewards():
            self.price = self.game_product.get_price() * (1 - 0.1 * number_of_rewards)
        return self.price

    def make_payment():
        payment = Payment(self.member.get_payment_method().get_account());
        return payment.pay(self.price)

    def record_purchase:
        record = PaymentRecord(self.member, self.game_product)
        return record

class Payment:

    def __init__(self, account):
        self.account = account

    def pay(amount):
        return True
