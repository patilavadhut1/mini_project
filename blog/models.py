from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return self.title




