from django.db import models
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
# class Post(models.Model):
#     author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     title=models.CharField(max_length=200)
#     text=models.TextField()
#     create_date=models.DateTimeField(default=timezone.now)
#     published_date=models.DateTimeField(blank=True,null=True)

#     def publish(self):
#         self.published_date=timezone.now()
#         self.save()

#     def approve_comments(self):
#         return self.comments.filter(approved_comments=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('post_detail',kwargs={'pk':self.pk})


# class Comment(models.Model):
#     post=models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
#     author=models.CharField(max_length=200)
#     text=models.TextField()
#     create_date=models.DateTimeField(default=timezone.now)
#     approved_comments=models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comments=True
#         self.save()

#     def __str__(self):
#         return self.text

#     def get_absolute_url(self):
#         return reverse('post_list')


class jee_mains(models.Model): 
    url   = models.CharField(max_length=1000, default="", null=True)
    year  =  models.IntegerField() 
    date  = models.IntegerField()
    month  = models.IntegerField()
    shift  = models.CharField(max_length=100, default="", null=True)
    question = models.TextField()
    options = ArrayField(models.CharField(max_length=5000, default=[]))
    question_images = ArrayField(models.CharField(max_length=5000, default=[]))
    solution_images = ArrayField(models.CharField(max_length=5000, default=[]))
    correct_option = models.CharField(max_length=100, default="", null=True)
    solution = models.TextField()
    times_loaded = models.CharField(max_length=1000, default="", null=True)
  