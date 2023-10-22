from django.db import models
from django.contrib.auth.models import User
from django.db.models import DO_NOTHING


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=DO_NOTHING)
