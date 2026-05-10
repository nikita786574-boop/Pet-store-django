from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100, unique = True)

    def same(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length = 20, verbose_name='Size name')

    def __str__(self):
        return self.name
    
class ProductSize(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE,
                                related_name = 'product_sizes', verbose_name = 'Product productsize')
    size = models.ForeignKey(to = Size, on_delete = models.CASCADE, related_name = 'size_products',
                             verbose_name = 'Size productsize')
    stock = models.PositiveIntegerField(default = 0, verbose_name = 'Stock productsize')

    def __str__(self):
        return f'{self.size.name} ({self.stock} in stock) for ({self.product.name}) '

class Product(models.Model):

    name = models.CharField(max_length = 100, verbose_name = 'Name product')
    slug = models.CharField(max_length = 100, unique = True, verbose_name = 'Slug product')
    category = models.ForeignKey(to=Category, on_delete = models.CASCADE, 
                                 related_name = 'products', verbose_name = 'Category product')
    color = models.CharField(max_length = 100, verbose_name = 'Color product')
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Price product')
    description = models.TextField(blank=True, max_length=1000)
    main_image = models.ImageField(upload_to='products/main/', verbose_name='Image product')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created at product')    
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated at product')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
         return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(to = Product, on_delete = models.CASCADE,
                                related_name = 'images', verbose_name = 'Product productimage')
    image = models.ImageField(upload_to='products/extra/', verbose_name = 'Image productimage')

