"""bullet_journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('task', views.TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name="task_detail"),
    path('event', views.EventListView.as_view(), name="event_list"),
    path('event/<int:pk>', views.EventDetailView.as_view(), name="event_detail"),
    path('note', views.NoteListView.as_view(), name="note_list"),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name="note_detail"),
    path('task-state', views.TaskStateListView.as_view(), name="task_state_list"),
    path('task-state/<int:pk>', views.TaskStateDetailView.as_view(), name="task_state_detail"),
    path('collection', views.JournalCollectionListView.as_view(), name="collection_list"),
    path('collection/<int:pk>', views.JournalCollectionDetailView.as_view(), name="collection_detail"),
    # path('day', views.DayView.as_view(), name="day_view"),
    # path('month/<int:pk>', views.MonthView.as_view(), name="month_view"),
]
