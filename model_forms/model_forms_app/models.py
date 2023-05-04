from django.db import models
# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name_plural='User'
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    email=models.EmailField()
    def __str__(self):
        return self.first_name