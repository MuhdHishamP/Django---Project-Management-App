from django.db import models

# Create your models here.
class Pro_add(models.Model):
    Project_Title = models.CharField(max_length=100)
    Project_Description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True)



    def __str__(self):
        return self.Project_Title
    

class task_add(models.Model):
    open = models.ForeignKey(Pro_add, on_delete=models.CASCADE, related_name="task_add")
    task = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task