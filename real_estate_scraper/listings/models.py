from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        unique_together = [("username", "agency")]

    def __str__(self):
        return self.email

class Listing(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=30, null=True)
    # TODO make a choice field
    type = models.CharField(max_length=200)
    link = models.CharField(max_length=500, null=True)
    reference_number = models.CharField(max_length=100)
    pub_update = models.DateTimeField(default=timezone.now())
    agency = models.CharField(max_length=100, default = "Unknown")

    # class Meta:
    #     unique_together = [("agency", "reference_number")]

    def __str__(self):
        return self.reference_number


