from django.db import models

# Create your models here.
class intialco(models.Model):
    the_owner = models.CharField(max_length=100)
    the_shape = models.CharField(max_length=100)


    def __unicode__(self):
        return self

class supco(models.Model):
    co =models.ForeignKey(intialco,on_delete=models.CASCADE )
    co_area =models.IntegerField(default=50)