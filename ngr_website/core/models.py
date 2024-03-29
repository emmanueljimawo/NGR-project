from django.db import models

from contest.models import TimeStampModel

# Create your models here.


class EmailSubscription(TimeStampModel):
    email = models.EmailField(max_length=200)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

