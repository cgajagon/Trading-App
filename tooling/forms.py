from django.forms import ModelForm, BaseModelFormSet, DateField, DateInput, CharField, FileField
from django import forms
from tooling.models import Tool, Condition, Project, ProjectActivity
from django.shortcuts import get_object_or_404


class ToolForm(ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'
        
class ConditionForm(ModelForm):
    class Meta:
        model = Condition
        fields = '__all__'
        date_audited = DateField(            
            widget = DateInput(
                attrs= {
                        'type':'date',
                        }
            )
        )
class ConditionFilterForm(forms.Form):
    tool_id = forms.IntegerField()

class ProjectActionForm(forms.Form):
    model = ProjectActivity
    fields = '__all__'

    def get_initial(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return {
            'project_related':project,
        }