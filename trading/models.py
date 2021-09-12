from django.db import models

# Create your models here.
class Share(models.Model):
    name=models.CharField(max_length=100)
    amount=models.FloatField(default="0.00")
    currency = models.CharField(max_length=100)
    crypto_currency = models.CharField(max_length=100)
    profit_loss_amt = models.FloatField(default="0.00")
    status = models.CharField(max_length=100)
    description=models.TextField(default=None)
    share_date=models.DateTimeField(default=None)

    def __str__(self):
        return self.name