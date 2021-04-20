from django.db import models

class Contact(models.Model):
    Name= models.CharField(max_length=50)
    ID = models.IntegerField(primary_key=True)
    EmailID=models.EmailField(max_length=50)
    Address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.Name
