from django import forms
from django.forms import HiddenInput
from  trading import models, widgets

class WatchSymbolForm(forms.ModelForm):
    class Meta:
        model = models.WatchSymbols
        fields = '__all__'
        widgets = {
            'notes':forms.Textarea(attrs={
                'rows':2,
            }),
            'symbol': widgets.Select2Widget(attrs={
            })
        }

class AlertWatchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlertWatchForm, self).__init__(*args, **kwargs)
        self.fields['watched_symbol'].widget = HiddenInput()

    class Meta:
        model = models.AlertWatch
        fields = '__all__'