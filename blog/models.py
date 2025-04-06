from django.db import models
from django.urls import reverse  # new
 
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True ,default="Not mentioned by the seller" , null=True)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):  # new
        return reverse("post_detail", kwargs={"pk": self.pk})
# Create your models here.
