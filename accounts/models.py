from django.contrib.auth.models import User
from django.db import models


class UserStripe(models.Model):
    user = models.OneToOneField(User)
    stripe_id = models.CharField(max_length=120)

    def __unicode__(self):
        return unicode(self.stripe_id)

