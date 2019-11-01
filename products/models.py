from django.db import models

CATEGORY_CHOICES = (
    ('ROH', 'ROH'),
    ('AEW', 'AEW'),
    ('WWE', 'WWE'),
    ('NJPW', 'NJPW'),
    ('IMPACT WRESTLING', 'Impact Wrestling'),
)

class Product(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, verbose_name='Company')
    slug = models.SlugField(max_length=250, null=True, blank=True)
    release_date = models.DateField()
    summary = models.CharField(max_length=150)
    description = models.TextField()
    user_likes = models.IntegerField(default=0, verbose_name='Like', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return "{0}-{1}".format(self.title, self.category)