from django.contrib.auth.signals import user_logged_in
import stripe

from .models import UserStripe

def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(email=user.email)
        user_stripe = UserStripe(user=user, stripe_id=customer.id)
        user_stripe.save()
    print customer

user_logged_in.connect(get_or_create_stripe)
