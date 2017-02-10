from django.db import models
from myapp_1 import views

# Create your models here.

class issue(models.Model):
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    define = models.TextField()

    THREATENING = 'YES'
    NON_THREATENING = 'NO'
    if_a_threat = (
            (THREATENING,'Threatening'),
            (NON_THREATENING,'Non-Threatening'),
            )
    threat = models.CharField(max_length=3,
                              choices=if_a_threat,
                              default='Select',)

    def __str__(self):
        return self.name
