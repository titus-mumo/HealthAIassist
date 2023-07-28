from django.db import models
from .models import CustomUser
from .models2 import Doctor
class TransactionApproval(models.Model):
    process_id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length = 255)
    checkout_request_id = models.CharField(max_length = 255)
    response_code = models.CharField(max_length=10)
    response_description = models.TextField()
    amount = models.IntegerField()
    mpesa_receipt_number = models.CharField(max_length=30)
    transaction_date = models.DateTimeField()
    phone_number = models.IntegerField()
    payment_status = models.IntegerField()

class LocationsViewed(models.Model):
    location_id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)