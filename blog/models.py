from django.db import models
from django.urls import reverse

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_details", kwargs={"pk": self.pk})
    