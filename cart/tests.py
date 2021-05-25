from django.test import TestCase

user = self.request.user
if not user.customer.stripe_customer_id:
    stripe_customer = stripe.Customer.create(email=user.email)
    user.customer.stripe_customer_id = stripe_customer["id"]
    user.customer.save()

order = get_or_set_order_session(self.request)

payment_intent = stripe.PaymentIntent.create(
    amount=order.get_raw_total(),
    currency='usd',
    customer=user.customer.stripe_customer_id,
)

payment_record, created = StripePayment.objects.get_or_create(
    order=order
)
payment_record.payment_intent_id = payment_intent["id"],
payment_record.amount = order.get_total()
payment_record.save()