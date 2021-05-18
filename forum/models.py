from django.db import models

# Create your models here.

class Comment(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
