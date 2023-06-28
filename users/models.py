from django.db import models
from django.contrib.auth.models import AbstractUser

# id, pw, nickname, email, phone, board_num
class User(AbstractUser):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    
    age = models.PositiveBigIntegerField(default=0)
    gender = models.CharField(max_length=30)
    
    is_business = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} / {self.age} /{self.description}"