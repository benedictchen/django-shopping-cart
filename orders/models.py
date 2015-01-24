from django.db import models
from carts.models import Cart


ORDER_STATUS = (
    ('started', 'Started'),
    ('abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)


class Order(models.Model):
    order_id = models.CharField(unique=True, max_length=120, default='abc')
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=255, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



