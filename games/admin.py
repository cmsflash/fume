from django.contrib import admin

from .models import Game, Item, FeaturedGame


admin.site.register(Game)
admin.site.register(Item)
admin.site.register(FeaturedGame)
