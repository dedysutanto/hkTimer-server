import uuid
import datetime
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    # img_file = models.ImageField()
    duration = models.PositiveIntegerField(default=0)
    limit = models.PositiveIntegerField(default=10)
    isWarning = models.BooleanField(default=False)
    isTimerRunning = models.BooleanField(default=False)
    isClicked = models.BooleanField(default=False)
    isMainMenu = models.BooleanField(default=False)
    # uuid = models.UUIDField(null=True)
    # start_time = models.DateTimeField(null=True, blank=True)
    # end_time = models.DateTimeField(null=True, blank=True)
    start_time = models.BigIntegerField(default=0)
    end_time = models.BigIntegerField(default=0)
    displayed_item = models.PositiveIntegerField(default=0)
    wasted_item = models.PositiveIntegerField(default=0)
    left_time = models.PositiveIntegerField(default=0)

    # For Menu leveling
    level = models.PositiveIntegerField(default=3)

    def __str__(self):
        return '%s %s' % (self.name, self.level)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])


class ProductCounter(models.Model):
    # uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, default=1)
    start_time = models.BigIntegerField(default=0)
    end_time = models.BigIntegerField(default=0)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    displayed_item = models.PositiveIntegerField(default=0)
    wasted_item = models.PositiveIntegerField(default=0)
    sold_item = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.product)

    def save(self, *args, **kwargs):
        self.start_datetime = timezone.make_aware(
            datetime.datetime.fromtimestamp(self.start_time),
            timezone.get_default_timezone())
        self.end_datetime = timezone.make_aware(
            datetime.datetime.fromtimestamp(self.end_time),
            timezone.get_default_timezone())
        self.sold_item = ((self.displayed_item - self.wasted_item) / self.displayed_item) * 100
        # self.start_datetime = datetime.date.fromtimestamp(self.start_time)
        #self.end_datetime = datetime.date.fromtimestamp(self.end_time)
        self.full_clean()
        super(ProductCounter, self).save(*args, **kwargs)


class ProductCounterSummary(ProductCounter):
    class Meta:
        proxy = True
        verbose_name = 'ProductCounter Summary'
        verbose_name_plural = 'ProductCounters Summary'