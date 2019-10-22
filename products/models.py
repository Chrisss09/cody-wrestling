from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=10)
    release_date = models.DateField()
    summary = models.CharField(max_length=150)
    description = models.TextField()
    user_likes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __unicode__(self):
        return self.title