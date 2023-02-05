from django.urls iport pathfrom issues import views

urlpatterns = [
    path("", views.IssueListView.as_view(), name="issue_list")
    path("<int:pk>/", views.IssueDetailView.as_view(), name="issue_detail"),
    path("<int:pk>/", views.IssueUpdateView.as_view(), name="issue_edit"),
    path("<int:pk>/", views.IssueDeletelView.as_view(), name="issue_delete"),
    path("new/", views.CreateView.as_view(), name="issue_new"),
]