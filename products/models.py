from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
