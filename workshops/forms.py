from typing import Any
from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Workshop, WorkshopPhoto, WorkshopDocument


MAX_UPLOAD_MB = 10
MAX_UPLOAD_BYTES = MAX_UPLOAD_MB * 1024 * 1024


def validate_file_size(f):
    if f and f.size > MAX_UPLOAD_BYTES:
        raise ValidationError(f"File too large (>{MAX_UPLOAD_MB} MB)")


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = [
            'title', 'topic', 'start_date', 'end_date', 'city', 'state', 'institute', 'online_link',
            'mode', 'coordinator_email', 'coordinator_phone', 'registration_link', 'agenda_pdf',
            'status', 'participants_count', 'category', 'feedback_form_link',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_agenda_pdf(self):
        f = self.cleaned_data.get('agenda_pdf')
        if f:
            validate_file_size(f)
            name = f.name.lower()
            if not name.endswith('.pdf'):
                raise ValidationError('Agenda must be a PDF file')
        return f

    def clean(self):
        cleaned = super().clean()
        mode = cleaned.get('mode')
        online_link = cleaned.get('online_link')
        city = cleaned.get('city')
        institute = cleaned.get('institute')
        if mode == Workshop.Mode.ONLINE and not online_link:
            self.add_error('online_link', 'Online link is required for online mode')
        if mode == Workshop.Mode.PHYSICAL and not (city or institute):
            self.add_error('city', 'City or Institute is required for physical mode')
        return cleaned


class WorkshopPhotoForm(forms.ModelForm):
    class Meta:
        model = WorkshopPhoto
        fields = ['image', 'caption']

    def clean_image(self):
        f = self.cleaned_data.get('image')
        if f:
            validate_file_size(f)
        return f


class WorkshopDocumentForm(forms.ModelForm):
    class Meta:
        model = WorkshopDocument
        fields = ['doc_type', 'file']

    def clean_file(self):
        f = self.cleaned_data.get('file')
        if f:
            validate_file_size(f)
            name = f.name.lower()
            if not name.endswith('.pdf'):
                raise ValidationError('Only PDF documents are allowed')
        return f


WorkshopPhotoFormSet = inlineformset_factory(
    Workshop, WorkshopPhoto, form=WorkshopPhotoForm, extra=3, can_delete=True
)

WorkshopDocumentFormSet = inlineformset_factory(
    Workshop, WorkshopDocument, form=WorkshopDocumentForm, extra=2, can_delete=True
)


class LoginForm(forms.Form):
    username = forms.CharField(label='Email or Username')
    password = forms.CharField(widget=forms.PasswordInput)
