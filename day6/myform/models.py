from django.db import models

# Create your models here.
# models.py
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    
class Meta:
    verbose_name ="Contact Form"
    verbose_name_plural ="Feedback Response"