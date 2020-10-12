from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    # Good practice: Add str() methods to models
    def __str__(self):

        # Display first 50 characters from text object
        return self.text[:50]
