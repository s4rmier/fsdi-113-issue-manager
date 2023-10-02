from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Issue
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/create-issue.html"
    model = Issue
    fields = ["summary", "description", "assignee", "status", "priority"]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)


class IssueUpdateView(UpdateView):
    template_name = "issues/update-issue.html"
    model = Issue
    fields = ["summary", "description", "status", "priority", "assignee"]
    success_url = reverse_lazy("list")


class IssueDeleteView(DeleteView):
    template_name = "issues/delete-issue.html"
    model = Issue
    success_url = reverse_lazy("list")


class IssueDetailView(DetailView):
    template_name = "issues/issue-detail.html"
    model = Issue


class IssueListView(ListView):
    template_name = "issues/issue-list.html"
    model = Issue
