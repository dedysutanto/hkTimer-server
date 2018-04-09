import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(default=0)
    limit = models.PositiveIntegerField(default=10)
    isWarning = models.BooleanField(default=False)
    isTimerRunning = models.BooleanField(default=False)
    isClicked = models.BooleanField(default=False)
    # uuid = models.UUIDField(null=True)
    # start_time = models.DateTimeField(null=True, blank=True)
    # end_time = models.DateTimeField(null=True, blank=True)
    start_time = models.BigIntegerField(default=0)
    end_time = models.BigIntegerField(default=0)
    displayed_item = models.PositiveIntegerField(default=0)
    wasted_item = models.PositiveIntegerField(default=0)
    left_time = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s' % (self.name)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])


class ProductCounter(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    displayed_item = models.PositiveIntegerField(default=0)
    wasted_item = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s' % (self.uuid)