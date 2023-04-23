from django.db import models


class JobDetails(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
