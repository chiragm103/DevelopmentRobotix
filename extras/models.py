from django.db import models

# Create your models here.
class FYI(models.Model):
    head = models.CharField(max_length=50,default='')
    title = models.CharField(max_length=100)
    link = models.URLField()
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.head


class DIY(models.Model):

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/diy')
    desc = models.CharField(max_length=1000)
    mentor = models.CharField(max_length=50)
    members = models.CharField(max_length=200)
    file = models.FileField(upload_to='docs/diy',default='')

    def __str__(self):

        return self.title
