from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null= True)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def is_completed(self):
        return self.finished_at is not None
    
    def __str__(self):
        return self.title
