from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    title = models.CharField(max_length = 32)
    description = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    picture = models.URLField()

    def __str__(self):
        return f"{self.id} : Title = {self.title}, Text = {self.description}"


class Comment(models.Model):
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.comment} (about {self.item})"
