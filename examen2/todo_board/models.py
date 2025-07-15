from django.db import models

# Create your models here.

class ToDo(models.Model):
    todo_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    user_id = models.BigIntegerField()


