from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    click_count = models.PositiveIntegerField(default=0)
    display = models.PositiveIntegerField(default=0)
    wasted = models.PositiveIntegerField(default=0)
    limit = models.PositiveIntegerField(default=10)
    isWarning = models.BooleanField(default=False)
    isTimerRunning = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])
