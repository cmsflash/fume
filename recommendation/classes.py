from purchase.models import PurchaseRecord
from tags.models import Tag
from games.models import Game

class Recommender(object):

    @staticmethod
    def make_recommendations(member):
        
        purchase_records = PurchaseRecord.objects.get_purchase_records_of(member)
        purchased_games = set()

        for purchase_record in purchase_records:
            purchased_games.add(purchase_record.item.game)

        recommendations = set()
        
        for i in range(min(len(purchase_records), 3)):
            purchase_record = purchase_records[i]
            reference_game = purchase_record.item.game
            reference_tags = set(Tag.objects.get_tags_of_game(reference_game))
            recommendation = [None, -1]
            for game in Game.objects.all():
                if not game in purchased_games:
                    tags = set(Tag.objects.get_tags_of_game(game))
                    similarity = len(tags.intersection(reference_tags))
                    if similarity > recommendation[1]:
                        recommendation[0] = game
                        recommendation[1] = similarity
            if not recommendation[1] == -1:
                recommendations.add(recommendation[0])

        return list(recommendations)
