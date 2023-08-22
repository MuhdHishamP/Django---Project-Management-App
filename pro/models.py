from django.db import models

# Create your models here.
class Pro_add(models.Model):
    Project_Title = models.CharField(max_length=100)
    Project_Description = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title}"