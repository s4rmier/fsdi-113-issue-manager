from django.urls import path
from issues import views

urlpatterns = [
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/delete/", views.IssueDeleteView.as_view(), name="delete"),
    path("<int:pk>/detail/", views.IssueDetailView.as_view(), name="detail"),
    path("", views.IssueListView.as_view(), name="list")
]
