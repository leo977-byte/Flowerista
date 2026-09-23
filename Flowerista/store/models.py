from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Lilies", "Papatya (Daisy)"
    slug = models.SlugField(unique=True)
    description = models.TextField()
    material = models.CharField(max_length=100, default="Handmade Crochet Cotton Yarn")
    shipping_days = models.IntegerField(default=3, help_text="Estimated delivery time in days")
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True, default="https://images.unsplash.com/photo-1563241527-3004b7be0ffd?w=500")

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    color_name = models.CharField(max_length=50)  # e.g., "Blossom Pink", "Papatya Yellow"
    color_hex = models.CharField(max_length=7, default="#E8839B") # HEX code used by CSS dynamic switcher
    stock_quantity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.product.name} - {self.color_name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.variant.product.base_price * self.quantity