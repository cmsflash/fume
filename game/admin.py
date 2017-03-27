from django.contrib import admin

# Register your models here.
from .models import Game
from .models import GameProduct
from .models import Image

admin.site.register(Game)
admin.site.register(GameProduct)
admin.site.register(Image)
