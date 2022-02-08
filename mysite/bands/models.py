from django.db import models

# Create your models here.


class Band(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"
