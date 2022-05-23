from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# from django import forms

# Create your models here.
OTT_CHOICES = (
    ('넷플릭스', '넷플릭스'),
    ('왓챠', '왓챠'),
    ('디즈니+', '디즈니+'),
    ('웨이브', '웨이브')
    )
# choices=OTT_CHOICES, widget=forms.CheckboxSelectMultiple

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    point = models.IntegerField(null=True)
    using_ott = MultiSelectField(choices=OTT_CHOICES, null=True)

