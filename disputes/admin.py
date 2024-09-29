from django.contrib import admin
from .models import Return, Order, Dispute

admin.site.register((
    Return,
    Order,
    Dispute,
))
