from django.contrib import admin

# Register your models here.

from chat.models import *

# Register your models here.

admin.site.register(Room)
admin.site.register(Message)