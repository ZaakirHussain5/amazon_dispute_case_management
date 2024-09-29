from django.db import migrations
from django.utils import timezone
import random


def populate_data(apps, schema_editor):
    Order = apps.get_model('disputes', 'Order')
    Return = apps.get_model('disputes', 'Return')
    Dispute = apps.get_model('disputes', 'Dispute')

    # Sample data for customers
    customer_names = ["John Doe", "Jane Smith", "Michael Brown", "Emily Davis", "Chris Johnson"]
    customer_emails = ["john@example.com", "jane@example.com", "michael@example.com", "emily@example.com", "chris@example.com"]
    customer_phones = ["+1-555-1234567", "+1-555-2345678", "+1-555-3456789", "+1-555-4567890", "+1-555-5678901"]
    customer_addresses = [
        "123 Maple Street, Springfield, IL",
        "456 Oak Avenue, Riverside, CA",
        "789 Pine Lane, Mountain View, CA",
        "101 Elm Drive, Orlando, FL",
        "202 Birch Boulevard, Dallas, TX"
    ]

    # Sample item names
    item_names = ["Headphones", "iPhone 13", "Door Mat", "Bluetooth Speaker", "Laptop"]

    # Step 1: Populate Orders
    orders = []
    for i in range(1, 11):
        name = random.choice(customer_names)
        email = random.choice(customer_emails)
        phone = random.choice(customer_phones)
        address = random.choice(customer_addresses)

        customer_details = f"{name}\n{email}\n{phone}\n{address}"
        item_name = random.choice(item_names)

        orders.append(Order(
            order_id=f'O{timezone.now().strftime("%d%m%Y")}-{i}',
            item_name=item_name,
            customer_details=customer_details,
            order_date=timezone.now()
        ))
    Order.objects.bulk_create(orders)

    # Step 2: Populate Returns
    returns = []
    for i, order in enumerate(Order.objects.all(), start=1):
        return_tracking_status = 0 if i % 2 == 0 else 1
        returns.append(Return(
            order=order,
            return_reason=f"Product {order.item_name} was defective",
            return_tracking=return_tracking_status
        ))
    Return.objects.bulk_create(returns)

    # Step 3: Populate Disputes
    disputes = []
    for i, return_item in enumerate(Return.objects.all(), start=1):
        dispute_reason = 0 if i % 2 == 0 else 1
        disputes.append(Dispute(
            order=return_item.order,
            return_item=return_item,
            dispute_reason_type=dispute_reason,
            dispute_reason_description=f"Customer had an issue with the {return_item.order.item_name}.",
            status=0,
        ))
    Dispute.objects.bulk_create(disputes)


class Migration(migrations.Migration):
    dependencies = [
        ("disputes", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]

