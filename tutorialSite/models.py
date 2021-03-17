from django.db import models 

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(default=0)
    imgUrl = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)

    def _str_(self):
        return self.title
        