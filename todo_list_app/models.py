from django.db import models


class TodoListItens(models.Model):
    content = models.TextField()