from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    account_number = models.CharField(max_length=100, unique=True)
