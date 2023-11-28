import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def checkout_link(instance):
    """ Getting the payment link using Stripe object instances Product, Price and Checkout Session """
    course_to_buy = stripe.Product.create(
      name=instance.paid_course.name
    )

    course_price = stripe.Price.create(
      unit_amount=instance.paid_amt,
      currency="eur",
      product=course_to_buy['id']
    )

    checkout = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": course_price['id'],
                "quantity": 1,
            },
        ],
        mode="payment",
    )

    return checkout['url']
