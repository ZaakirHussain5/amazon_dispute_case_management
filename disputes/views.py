from django.shortcuts import render
from .models import Dispute, Order, Return

def index(request):
    return render(request, "index.html", {
        "disputes": (
            Dispute.objects.all()
            .select_related(
                "order",
                "return_item"
            )
        )
    })

def new_dispute(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        return_id = request.POST.get("return_id")
        status = request.POST.get("status")
        dispute_reason_type = request.POST.get("dispute_reason_type")
        dispute_reason_description = request.POST.get("resolution", "")
        resolution = request.POST.get("resolution", "")

        dispute = Dispute(
            order_id=order_id,
            return_item_id=return_id,
            status=status,
            dispute_reason_type=dispute_reason_type,
            dispute_reason_description=dispute_reason_description,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            resolution=resolution
        )

        new_dispute = dispute.save()

        return render(request, "disputes/dispute_row.html", {
            "dispute": new_dispute
        })
    
    return render(request, "disputes/dispute_form.html", {
        "orders": Order.objects.all(),
        "return_items": Return.objects.all(),
        "dispute_reason_type_choices": dict(Dispute.DISPUTE_REASON_TYPE_CHOICES),
        "dispute_status_choices": dict(Dispute.STATUS_CHOICES)
    })

def edit_dispute(request, id):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        return_id = request.POST.get("return_id")
        status = request.POST.get("status")
        dispute_reason_type = request.POST.get("dispute_reason_type")
        dispute_reason_description = request.POST.get("resolution", "")
        resolution = request.POST.get("resolution", "")

        Dispute.objects.filter(
            id=id
        ).update(
            order_id=order_id,
            return_item_id=return_id,
            status=status,
            dispute_reason_type=dispute_reason_type,
            dispute_reason_description=dispute_reason_description,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            resolution=resolution
        )

        dispute = Dispute.objects.get(id=id)

        return render(request, "disputes/dispute_row.html", {
            "dispute": dispute
        })
    
    dispute = Dispute.objects.get(id=id)
    return render(request, "disputes/dispute_form.html", {
        "dispute": dispute,
        "orders": Order.objects.all(),
        "return_items": Return.objects.all(),
        "dispute_reason_type_choices": dict(Dispute.DISPUTE_REASON_TYPE_CHOICES),
        "dispute_status_choices": dict(Dispute.STATUS_CHOICES)
    })