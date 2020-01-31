from django.db import models
import time
import cv2

# Create your models here.
class UserManager(models.Manager):
    
    def logout_validator(self, postData):
        errors = {}

        if len(User.objects.filter(name=postData['name'])) < 1:
            errors['name'] = 'name does not exist'

        if len(User.objects.filter(username=postData['username'])) < 1:
            errors['username'] = 'username does not exist'

        return errors

    def login_validator(self, postData):
        errors = {}

        if len(postData['name']) == 0:
            errors['name'] = 'Must input name'

        if len(postData['username']) == 0:
            errors['username'] = 'Must input username'

        if len(postData['r_for_e']) == 0:
            errors['r_for_e'] = 'Must input reason for entering'

        if len(postData['company']) == 0:
            errors['company'] = 'Must input company name'

        if len(postData['location']) == 0:
            errors['location'] = 'Must input location name'
        return errors

    def create_user(self, postData, img_path):
        User.objects.create(
            name = postData['name'],
            username = postData['username'],
            r_for_e = postData['r_for_e'],
            company = postData['company'],
            location = postData['location'],
            img = img_path
        )

class AdminManager(models.Manager):
    
    def admin_validator(self, postData):
        errors = {}

        if len(Admin.objects.filter(email=postData['email'])) < 1:
            errors['email'] = 'Admin email invalid'

        if len(Admin.objects.filter(password=postData['password'])) < 1:
            errors['Password'] = 'Admin password invalid'

        return errors

class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = AdminManager()

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    r_for_e = models.TextField()
    in_time = models.TimeField(auto_now_add=True)
    out_time = models.BooleanField(default=False)
    company = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    objects = UserManager()
