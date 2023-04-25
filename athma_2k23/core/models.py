from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


User = get_user_model()
class Profiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(0)])
    semester = models.CharField(max_length=10, null=False)
    branch = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.user.username