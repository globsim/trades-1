from django.shortcuts import render


def index(request):
    args = {'title': 'Options Tools'}
    return render(request, 'options/index.html', args)
