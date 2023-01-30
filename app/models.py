from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['title']
    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    image  = models.ImageField(upload_to='product_image')
    prize = models.DecimalField(max_digits=8,decimal_places=2)
    dis = models.TextField(max_length=600)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    @property
    def related(self):
        return self.category.products.all().exclude(pk = self.pk)


class slider(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='Banner')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
        return self.title
