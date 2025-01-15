from django.db import models
from django.contrib.auth import get_user_model

from apps.product.models import Product

User = get_user_model()


class Rating(models.Model):
    RATING_CHOICES = (
        (1.0, 'Too bad'),
        (2.0, 'Bad'),
        (3.0, 'ok'),
        (4.0, 'good'),
        (5.0, 'excellent')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.DecimalField(choices=RATING_CHOICES, max_digits=1, decimal_places=1)


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


