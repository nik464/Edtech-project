from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('workshops/', views.WorkshopListView.as_view(), name='workshop-list'),
    path('workshops/<int:pk>/', views.WorkshopDetailView.as_view(), name='workshop-detail'),
    path('workshops/new/', views.WorkshopCreateView.as_view(), name='workshop-create'),
    path('workshops/<int:pk>/edit/', views.WorkshopUpdateView.as_view(), name='workshop-edit'),
    path('workshops/<int:pk>/uploads/', views.manage_uploads, name='workshop-uploads'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('export/excel/', views.export_excel, name='export-excel'),
    path('export/pdf/', views.export_pdf, name='export-pdf'),
]