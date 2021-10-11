from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_pw = models.IntegerField()

    def __str__(self) -> str:
        return self.user_name

