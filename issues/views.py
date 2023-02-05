from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models imprt Issue


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue


class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue


class IssueUpdateView(UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["title", "summary", "description", "assignee", "status"]

class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["title", "summary", "description", "assignee", "status"]

class IssueDeleteView(DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("issue_list")


# Create your views here.
