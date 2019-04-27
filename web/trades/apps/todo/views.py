from django.shortcuts import render, redirect, get_object_or_404
from redis import Redis
from .models import (Item)

try:
    redis = Redis(host='redis', port=6379)
except Exception:
    pass


def index(request):
    print('--------')
    print(request.method)
    print('--------')

    if request.method == 'POST':
        print('---2-----')
        print(request.POST['item_text'])
        Item.objects.create(text=request.POST['item_text'])

        print('---21-----')

        # return redirect('/')
    items = Item.objects.all()
    counter = 100
    try:
        counter = redis.incr('counter')
    except Exception:
        pass
    print('--------')
    print(1)
    print('--------')
    return render(request, 'todo/index.html', {'items': items, 'counter': counter})
