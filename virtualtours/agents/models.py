from django.db import models
from django.utils import timezone

# Create your models here.
class Agent(models.Model):
  name = models.CharField(max_length=200)
  region = models.CharField(max_length=200)
  doj = models.DateTimeField('Date Joined')
  contact = models.BigIntegerField()
  email = models.EmailField()

  def __str__(self):
        return self.name