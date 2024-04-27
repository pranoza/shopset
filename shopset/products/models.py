from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Products(models.Model):
  Title = models.CharField(max_length=100)
  slug = models.CharField(max_length=100)
  date_created = models.DateField(auto_now_add=True)
  date_updated = models.DateField(auto_now=True)
  description = RichTextField()