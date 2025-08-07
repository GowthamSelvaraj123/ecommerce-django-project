from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='products',
        null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    rating = models.FloatField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    tags = models.JSONField(blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    weight = models.FloatField(null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    depth = models.FloatField(null=True, blank=True)
    warranty_information = models.CharField(max_length=255, blank=True, null=True)
    shipping_information = models.CharField(max_length=255, blank=True, null=True)
    availability_status = models.CharField(max_length=50, blank=True, null=True)
    return_policy = models.CharField(max_length=255, blank=True, null=True)
    minimum_order_quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    qr_code = models.URLField(blank=True, null=True)
    images = models.JSONField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}★"
