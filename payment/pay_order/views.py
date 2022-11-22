import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'success.html'


class ItemLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs['id'])
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update(
            {
                'Item': item,
                'stripe_publishable_key': settings.STRIPE_PUBLIC_KEY
            }
        )
        return context


class CreateCheckoutSessionView(View):
    # @csrf_exempt
    def get(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://127.0.0.1:8000/pay_order'
        item_id = self.kwargs['id']
        item = Item.objects.get(id=item_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price*100),
                    },
                    "quantity": 1
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel'))
        )
        return JsonResponse(
            {
                 'id':  checkout_session.id
            }
        )
