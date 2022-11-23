from django.contrib import admin
from django.urls import path

from .views import (CreateCheckoutSessionView,
                    ItemLandingPageView,
                    OrderPageView,
                    SuccessView,
                    CancelView,
                    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<id>/', ItemLandingPageView.as_view(), name='item'),
    path('order/<id>/', OrderPageView.as_view(), name='order'),
    path('buy/<id>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('buy_order/<id_order>/', CreateCheckoutSessionView.as_view(), name='buy_order'),
]
