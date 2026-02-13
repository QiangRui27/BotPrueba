from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('api/total-leads/', views.api_total_leads, name='api_total_leads'),
    path('api/leads-por-dominio/', views.api_leads_por_dominio, name='api_leads_por_dominio'),
    path('telegram/', views.telegram_webhook, name='telegram_webhook'),
    path('api/leads/<int:id>/edit/', views.edit_lead_api, name='edit_lead_api'),
    path('api/leads/<int:id>/delete/', views.delete_lead_api, name='delete_lead_api'),
]
