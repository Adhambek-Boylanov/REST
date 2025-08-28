from datetime import timezone

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Movie(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    photo=models.ImageField(upload_to='photos/%Y/%m/%d', null=True,blank=True)
    genre=models.CharField(max_length=50)
    actor=models.ManyToManyField('Actor')

    def __str__(self):
        return self.name
class Actor(models.Model):
    name=models.CharField(max_length=150)
    birthdate=models.DateField()

    def __str__(self):
        return self.name

class CommitMovie(models.Model):
    title = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_ed = models.DateField(auto_now_add=True)
    update_ed = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
# class Product(models.Model):
#     title = models.CharField(max_length=50)
#     price = models.IntegerField()
#
#     def __str__(self):
#         return self.title
# class Sale(models.Model):
#     product = models.OneToOneField(Product,on_delete=models.CASCADE)
#     discount_percent = models.IntegerField()
#     start_time = models.DateField()
#     end_time = models.DateField()
#     def is_active(self):
#         now = timezone.now()
#         return self.start_time <= now <= self.end_time
#     class Meta:
#         unique_together = ('product','start_time','end_time')
#
