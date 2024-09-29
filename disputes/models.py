from datetime import datetime
from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True, blank=True)
    item_name = models.CharField(max_length=100)
    customer_details = models.TextField() # Can be extended to other model 
    order_date = models.DateTimeField()

    def __str__(self):
        return self.order_id

    def save(self, *args, **kwargs):
        if not self.order_id:
            today_date = datetime.now().strftime("%d%m%Y")
            count = Order.objects.all().count() + 1
            # 0DDMMYYYY-count
            self.order_id = f'O{today_date}-{count}'
        
        super(Order, self).save(*args, **kwargs)


class Return(models.Model):
    REQUESTED=0
    PROCESSING=1
    PICKUP_SCHEDULED=2
    PICKUP_COMPLETED=3
    CANCELED=4
    REFUND_COMPLETED=5

    RETURN_TRACKING_CHOICES=(
        (REQUESTED, "Requested"),
        (PROCESSING, "Processing"),
        (PICKUP_SCHEDULED, "Pickup Scheduled"),
        (PICKUP_COMPLETED, "Pickup Completed"),
        (CANCELED, "Canceled"),
        (REFUND_COMPLETED, "Refund Completed"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    return_reason = models.CharField(max_length=255)
    return_tracking = models.SmallIntegerField(choices=RETURN_TRACKING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Return of {self.order.order_id}"


class Dispute(models.Model):
    # Dispute type options
    BILLING=0
    SERVICE=1
    OTHER=2

    # Status options
    OPEN=0
    RESOLVED=1

    DISPUTE_REASON_TYPE_CHOICES=(
        (BILLING, "Billing"),
        (SERVICE, "Service"),
        (OTHER, "Other"),
    )

    STATUS_CHOICES = (
        (OPEN, 'Open'), 
        (RESOLVED, 'Resolved')
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    return_item = models.ForeignKey(Return, on_delete=models.CASCADE)
    dispute_reason_type = models.SmallIntegerField(choices=DISPUTE_REASON_TYPE_CHOICES)
    dispute_reason_description = models.TextField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
    resolution = models.TextField(null=True, blank=True)
