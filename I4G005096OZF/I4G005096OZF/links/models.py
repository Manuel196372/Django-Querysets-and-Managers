from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Post (models.Model) :
    target_url = models.URLField (maxlength=200)
    description = models.CharField(maxlength=200)
    identifier = models.SlugField(maxlength=20)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="posts"
    )
    created_date = models.DateTimeField()
    active =models.BooleanField(auto_now_add=True)
   
    def __str__(self):
        return self.title

object = models.Manager()
public = ActiveLinkManager()
