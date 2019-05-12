# oqiw45

from django.shortcuts import render, redirect
import time
from ib_insync import *
import asyncio
from random import randint


def index(request):
    args = {'title': 'Trading Options today'}
    return render(request, 'trading/index.html', args)


def currency_exchange(request, currencies='EURUSD'):
    df = None
    ll = {}
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        ll['1'] = 1
    except Exception:
        ll['1'] = 0
    try:
        ib_ = IB()
        ll['21'] = 1
        ll['2'] = ib_
    except Exception:
        ll['2'] = 0
    try:
        ci = randint(0, 10000)
        ll['3'] = 1
    except Exception:
        ll['3'] = 0



    try:
        ib_.connect('127.0.0.1', 4002, clientId=ci)
        ll['4'] = 1
    except Exception:
        ll['4'] = 0
        try:
            ib_.connect('127.0.0.1', 4002, clientId=ci)
            ll['41'] = 1
        except Exception:
            ll['41'] = 0
    try:
        print(ib_)
        c = Forex(currencies)
        bars = ib_.reqHistoricalData(c, endDateTime='', durationStr='1 D',
                                     barSizeSetting='1 min', whatToShow='MIDPOINT', useRTH=True)
        # print(bars)
        ll['5'] = 1
    except Exception:
        ll['5'] = 0

    context = {
        'll': ll,
        'df': df,
        'head': currencies,
        'title': 'Currency Exchange',
        'cur_list':['GBPUSD',
                    'GBPZAR',
                    'HKDJPY',
                    'KRWAUD',
                    'KRWCAD',
                    'KRWCHF',
                    'KRWEUR',
                    'KRWGBP',
                    'KRWHKD',
                    'KRWJPY',
                    'KRWUSD',
                    'MXNJPY',
                    'NOKJPY',
                    'NOKSEK',
                    'NZDCAD',
                    'NZDCHF',
                    'NZDJPY',
                    'NZDUSD',
                    'SEKJPY',
                    'SGDCNH',
                    'SGDJPY',
                    'TRYJPY',
                    'USDCAD',
                    'USDCHF',
                    'USDCNH',
                    'USDCZK',
                    'USDDKK',
                    'USDHKD',
                    'USDHUF',
                    'USDILS',
                    'USDJPY',
                    'USDKRW',
                    'USDMXN',
                    'USDNOK',
                    'USDPLN',
                    'USDRUB',
                    'USDSEK',
                    'USDSGD',
                    'USDTRY',
                    'USDZAR',
                    'ZARJPY',
                    'EURPLN',
                    'EURRUB',
                    'EURSEK',
                    'EURSGD',
                    'EURTRY',
                    'EURUSD',
                    'EURZAR',
                    'GBPAUD',
                    'GBPCAD',
                    'GBPCHF',
                    'GBPCNH',
                    'GBPCZK',
                    'GBPDKK',
                    'GBPHKD',
                    'GBPHUF',
                    'GBPJPY',
                    'GBPMXN',
                    'GBPNOK',
                    'GBPNZD',
                    'GBPPLN',
                    'GBPSEK',
                    'GBPSGD',
                    'GBPTRY',
                    'GBPUSD',
                    'GBPZAR',
                    'HKDJPY',
                    'KRWAUD',
                    'KRWCAD',
                    'KRWCHF',
                    'KRWEUR',
                    'KRWGBP',
                    'KRWHKD',
                    'KRWJPY',
                    'KRWUSD',
                    'MXNJPY',
                    'NOKJPY',
                    'NOKSEK',
                    'NZDCAD',
                    'NZDCHF',
                    'NZDJPY',
                    'NZDUSD',
                    'SEKJPY',
                    'SGDCNH',
                    'SGDJPY',
                    'TRYJPY',
                    'USDCAD',
                    'USDCHF',
                    'USDCNH',
                    'USDCZK',
                    'USDDKK',
                    'USDHKD',
                    'USDHUF',
                    'USDILS',
                    'USDJPY',
                    'USDKRW',
                    'USDMXN',
                    'USDNOK',
                    'USDPLN',
                    'USDRUB',
                    'USDSEK',
                    'USDSGD',
                    'USDTRY',
                    'USDZAR',
                    'ZARJPY']
    }


    return render(request, 'trading/currency_exchange.html', context)


def option_trading(request):
    title = 'Option Trading'
    return render(request, 'trading/index.html', {'title': title})


