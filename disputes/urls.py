from django.urls import path
from . import views

app_name="disputes"

urlpatterns = [
    path('', views.index, name="index"),
    path('new_dispute/', views.new_dispute, name="new_dispute"),
    path('dispute/<int:id>/', views.edit_dispute, name="edit_dispute"),
]