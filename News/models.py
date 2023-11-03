from django.db import models

# Create your models here.

class News(models.Model):
    Headline = models.CharField(max_length=200)
    Content = models.TextField(max_length=10000)
    Reporter = models.CharField(max_length=200)
    Images = models.ImageField(upload_to='News_image', blank=True, null=True)
    date_reported = models.DateTimeField(auto_now_add=None)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.Headline




    