import stripe
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .models import Item, Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


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


class OrderPageView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        order = Order.objects.get(id=self.kwargs['id'])
        order_items = OrderItem.objects.filter(order=order)
        context = super(OrderPageView, self).get_context_data(**kwargs)
        context.update(
            {
                'order': order,
                'order_items': order_items,
                'stripe_publishable_key': settings.STRIPE_PUBLIC_KEY
            }
        )
        return context


class CreateCheckoutSessionView(View):
    # @csrf_exempt
    def get(self, request, *args, **kwargs):
        items = []
        if kwargs.get('id') != None:
            item_id = self.kwargs['id']
            items.append({'item': Item.objects.get(id=item_id), 'quantity': 1})
        else:
            order = Order.objects.get(id=self.kwargs['id_order'])
            items = [{'item':order_item.item,
                      'quantity': order_item.quantity} for order_item in list(OrderItem.objects.filter(order=order))]
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item["item"].name,
                        },
                        'unit_amount': int(item["item"].price * 100),
                    },
                    "quantity": item['quantity']
                } for item in items
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel'))
        )
        return JsonResponse(
            {
                'id': checkout_session.id
            }
        )
