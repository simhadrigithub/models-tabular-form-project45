from django.db import models

# Create your models here.

class topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Topic_name

class webpage(models.Model):
    Topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

class accessrecord(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    
    def __str__(self):
        return self.author