from django.db import models

class College(models.Model): 
    id   = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=64) 
    img  = models.CharField(max_length=64)
    aimg = models.CharField(max_length=64)

    def __str__(self):
        return self.name 

class Block(models.Model): 
    id   = models.IntegerField(primary_key=True) 
    clg  = models.ForeignKey(College, on_delete=models.CASCADE) 
    name = models.CharField(max_length=64)
    img  = models.CharField(max_length=64)
    aimg = models.CharField(max_length=64)
    num  = models.IntegerField()

    def __str__(self): 
        return self.name 

class Floor(models.Model): 
    fid   = models.IntegerField() 
    clg   = models.ForeignKey(College, on_delete=models.CASCADE) 
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    name  = models.CharField(max_length=64)
    img   = models.CharField(max_length=64)
    aimg  = models.CharField(max_length=64)

    def __str__(self): 
        return self.name 
