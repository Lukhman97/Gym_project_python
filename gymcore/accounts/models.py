from django.db import models
from django.contrib.auth.models import User


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    membership_plan = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
