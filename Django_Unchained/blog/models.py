from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author =  models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey creates a many to one relationship, many posts can have one user and CASCADE means if user is deleted all their posts will be automatically deleted.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    