from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, FormView
from tooling.models import Tool, Condition, Project, ProjectActivity
from tooling.forms import ToolForm, ConditionForm, ConditionFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
import json


@login_required
def index(request):
    return render(request, 'index.html')

class ListToolingView(LoginRequiredMixin, ListView):
    model = Tool
    template_name = 'tooling/tooling.html'
    context_object_name = 'tool_list'

class DetailToolingView(LoginRequiredMixin, DetailView):
    model = Tool
    template_name = 'tooling/tooling_detail.html'

class CreateToolingView(LoginRequiredMixin, CreateView):
    model = Tool
    template_name = 'tooling/tooling_update.html'
    fields = '__all__'
    success_url = reverse_lazy('tooling:tooling')

class UpdateToolingView(UpdateView):
    model = Tool
    template_name = 'tooling/tooling_update.html'
    form_class = ToolForm

class DeleteToolingView(LoginRequiredMixin,DeleteView):
    model = Tool
    success_url = reverse_lazy('tooling:tooling')

class CreateToolingconditionView(LoginRequiredMixin, CreateView):
    model = Condition
    template_name = 'tooling/toolingcondition_new.html'
    form_class = ConditionForm
    success_url = reverse_lazy('tooling:tooling')

    def get_initial(self):
        tool = get_object_or_404(Tool, pk=self.kwargs.get('pk'))
        return {
            'tool_audited':tool,
        }

class FilterToolingconditionView(FormView):
    template_name = 'tooling/toolingcondition_filter.html'
    form_class = ConditionFilterForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('tooling:toolingcondition', kwargs = {'pk', })

class ListConditionView(ListView):
    model = Condition
    template_name = 'tooling/toolingcondition.html'

class DeleteToolingconditionView(LoginRequiredMixin,DeleteView):
    model = Condition
    success_url = reverse_lazy('tooling:tooling')

class ListProjectsView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'tooling/projects.html'
    context_object_name = 'project_list'

class DetailProjectView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'tooling/project_detail.html'

class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'tooling/toolingcondition_new.html'
    success_url = reverse_lazy('tooling:projects')
    fields = '__all__'