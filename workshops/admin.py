from django.contrib import admin
from .models import Workshop, WorkshopPhoto, WorkshopDocument


class WorkshopPhotoInline(admin.TabularInline):
    model = WorkshopPhoto
    extra = 1


class WorkshopDocumentInline(admin.TabularInline):
    model = WorkshopDocument
    extra = 1


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'start_date', 'end_date', 'mode', 'status', 'city', 'state', 'participants_count', 'reports_approved'
    )
    list_filter = ('status', 'mode', 'start_date', 'state', 'category')
    search_fields = ('title', 'topic', 'city', 'institute', 'coordinator__username')
    inlines = [WorkshopPhotoInline, WorkshopDocumentInline]


@admin.register(WorkshopPhoto)
class WorkshopPhotoAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'caption', 'uploaded_at')


@admin.register(WorkshopDocument)
class WorkshopDocumentAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'doc_type', 'uploaded_at')
