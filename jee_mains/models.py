from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
class jee_mains(models.Model): 
    # url   = models.CharField(max_length=1000, default="", null=True)
    url   = models.SlugField(max_length=1000, default="", null=True)
    year  = models.IntegerField(null=True) 
    date  = models.IntegerField(null=True)
    # month  = models.IntegerField()
    month  = models.CharField(max_length=100, default="", null=True)
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
    def get_absolute_url(self):
        return reverse("jee_mains_single", kwargs={"url": self.url})

class TestSeriesMap(models.Model):
    physics_ques_map = ArrayField(models.IntegerField(default=[]))
    chemistry_ques_map = ArrayField(models.IntegerField( default=[]))
    maths_ques_map = ArrayField(models.IntegerField(default=[]))
