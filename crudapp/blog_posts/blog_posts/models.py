from django.db import models

class CrudApp(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField(max_length=30)

    def __str__(self):
        return self.Name

