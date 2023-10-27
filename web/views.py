from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_expense(request):
    print(request.POST)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    date = datetime.now()
    if 'date' in request.POST:
        date = request.POST['date']
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok',
    }, encoder=DjangoJSONEncoder)


@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    date = datetime.now()
    if 'date' in request.POST:
        date = request.POST['date']
    Income.objects.create(user=this_user, amount=request.POST['amount'],
                          text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok',
    }, encoder=DjangoJSONEncoder)
