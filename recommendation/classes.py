from purchase.models import PurchaseRecord

def make_recommendation(member):
    purchase_records = PurchaseRecord.objects.get_purchase_records_of(member)
    for i in range(3):
        purchase_record = purchase_records[i]
        game = purchase_record.item.game
        pass
