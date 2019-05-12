from django.conf.urls import url
from django.urls import path
from .views import (index, currency_exchange, option_trading)

app_name = "trading"

urlpatterns = [
    url(r'^$', index, name='index'),
    path('currency_exchange', currency_exchange, name='currency_exchange'),
    path('currency_exchange/<currencies>', currency_exchange, name='currency_exchange_wc'),
    url(r'^option_trading$', option_trading, name='option_trading'),
]
