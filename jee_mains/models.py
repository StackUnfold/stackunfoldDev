from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
class jee_mains(models.Model): 
    url   = models.CharField(max_length=1000, default="", null=True)
    year  =  models.IntegerField() 
    date  = models.IntegerField()
    month  = models.IntegerField()
    shift  = models.CharField(max_length=100, default="", null=True)
    question = models.TextField()
    options = ArrayField(models.CharField(max_length=5000, default=[]))
    subject  = models.CharField(max_length=100, default="", null=True)
    question_images = ArrayField(models.CharField(max_length=5000, default=[],  null=True))
    solution_images = ArrayField(models.CharField(max_length=5000, default=[], null=True))
    option_images = ArrayField(models.CharField(max_length=5000, default=[] , null=True))
    correct_option = models.CharField(max_length=100, default="", null=True)
    solution = models.TextField()
    times_loaded = models.CharField(max_length=1000, default="", null=True)
  