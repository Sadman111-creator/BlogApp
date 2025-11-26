from django.db import models

class Category(models.Model):
        
    def __str__(self):
        return self.title

class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title