from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    sku = models.CharField(max_length=100, blank=False)
    origin = models.ForeignKey('Origin', on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    ingredients = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False, default=0)
    image = models.ImageField(blank=True, null=True)
    
    # Display <Product Name>:<Product ID>
    def __str__(self):
        return self.sku + " | " + self.name + " : " +  "Available Stock: " + str(self.quantity)
        # + self.quantity
    
    def getCostInDollars(self):
        return self.cost/100

class Origin(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name