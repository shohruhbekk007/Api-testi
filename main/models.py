from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name