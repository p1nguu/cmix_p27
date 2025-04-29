from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from .models import Presta
import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]


class PrestaForm(forms.ModelForm):
    class Meta:
        model = Presta
        exclude = ('pub_date',)
        widgets = {
            'presta_name': forms.TextInput(attrs={'class': 'form-control'}),
            'presta_date': forms.DateInput(format=('%d %b, %Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'presta_start': forms.Select(choices=HOUR_CHOICES),
            'presta_end': forms.Select(choices=HOUR_CHOICES),
        }
        help_texts = {
                'presta_comments': '<span class="help-text-white"> (Genres Musicaux souhaitées, Lien de Playlist, etc.)</span>',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('presta_name', css_class='mb-3'),
            Field('presta_date', css_class='mb-3'),
            Field('presta_start', css_class='mb-3'),
            Field('presta_end', css_class='mb-3'),
            Field('presta_comments', css_class='mb-3'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
