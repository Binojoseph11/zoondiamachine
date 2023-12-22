from site import USER_BASE
from django.db import models


class shortenedURl(models.Model):
    orginal_urls= models.URLField()
    short_url =models.CharField(max_length=10,unique=True)
    user= models.ForeignKey(USER_BASE,on_delete=models.CASCADE)

    