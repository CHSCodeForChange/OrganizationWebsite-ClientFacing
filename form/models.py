from django.db import models



class Group(models.Model):
    objects = models.Manager()

    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    comment = models.CharField(max_length=960)
    email = models.EmailField()
