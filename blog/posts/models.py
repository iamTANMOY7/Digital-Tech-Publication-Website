from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField(default="")
    post_description = models.TextField(default="")
    published_date = models.DateField(auto_now=True)
    post_authors = models.IntegerField()
    post_image = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return self.post_title
