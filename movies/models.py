from django.db import models

# Create your models here.
class Movies(models.Model):
    overview =  models.TextField(blank=True,null=True)
    release_date = models.DateField(blank=True,null=True)
    popularity = models.CharField(max_length=200,blank=True,null=True)
    vote_average = models.DecimalField(max_digits=2,decimal_places=1,blank=True,null=True)
    vote_num = models.IntegerField(blank=True,null=True)
    title = models.CharField(max_length=500,blank=True,null=True)
    video = models.BooleanField(default=False)
    number = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.title