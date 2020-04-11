from django.core.validators import MaxValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(validators=[MaxValueValidator(100000)])
    image_src = models.URLField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    # Date-Time fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Validation fields
    is_deleted = models.BooleanField(default=False)
