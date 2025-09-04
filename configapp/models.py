from datetime import timezone

from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self,username,password = None,**extra_fields):
        if not username:
            raise ValueError("Username kiritilishi shart")
        user = self.model(username = username,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_staff',True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser is_admin = True bo'lishi kerak")
        if extra_fields.setdefault('is_staff') is not True:
            raise ValueError("Superuser is_staff = True bo'lish kerak")

        return self.create_user(username,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    # phone_regex = RegexValidator(
    #     regex = r'^\+9989\d{9}$',
    #     message="telefon raqam tog'ri kelishi kerak"
    # )
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

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
