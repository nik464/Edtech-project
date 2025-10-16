from django.db import models
from django.contrib.auth.models import User


class Workshop(models.Model):
    class Mode(models.TextChoices):
        PHYSICAL = 'physical', 'Physical'
        ONLINE = 'online', 'Online'

    class Status(models.TextChoices):
        UPCOMING = 'upcoming', 'Upcoming'
        LIVE = 'live', 'Live'
        COMPLETED = 'completed', 'Completed'

    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True)
    institute = models.CharField(max_length=255, blank=True)
    online_link = models.URLField(blank=True)
    mode = models.CharField(max_length=20, choices=Mode.choices)

    coordinator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='coordinated_workshops')
    coordinator_email = models.EmailField()
    coordinator_phone = models.CharField(max_length=20)

    registration_link = models.URLField(blank=True)
    agenda_pdf = models.FileField(upload_to='agendas/', blank=True, null=True)
    feedback_form_link = models.URLField(blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPCOMING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    participants_count = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=120, blank=True)  # optional categorization
    state = models.CharField(max_length=120, blank=True)
    reports_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} ({self.start_date})"


def workshop_upload_path(instance, filename):
    return f"workshops/{instance.workshop_id}/{filename}"


class WorkshopPhoto(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=workshop_upload_path)
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Photo for {self.workshop.title}"


class WorkshopDocument(models.Model):
    class DocType(models.TextChoices):
        FEEDBACK_SUMMARY = 'feedback_summary', 'Feedback Summary'
        ATTENDANCE = 'attendance', 'Attendance Report'
        OTHER = 'other', 'Other'

    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='documents')
    doc_type = models.CharField(max_length=50, choices=DocType.choices)
    file = models.FileField(upload_to=workshop_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.get_doc_type_display()} - {self.workshop.title}"

# Create your models here.
