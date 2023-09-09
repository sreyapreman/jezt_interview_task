from django.db import models

class Todos(models.Model):
    task_name=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
