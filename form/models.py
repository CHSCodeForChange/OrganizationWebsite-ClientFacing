from django.db import models



class Organization(models.Model):
    objects = models.Manager()

    firstName = models.CharField(max_length=120, null=True)
    lastName = models.CharField(max_length=120, null=True)
    organization = models.CharField(max_length=120, null=True)
    comment = models.CharField(max_length=960, null=True)
    email = models.EmailField(null=True)
