from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.PostView.as_view()),
    path('home/<int:pk>/', views.CurrentPostView.as_view()),

    path('football/news/', views.PostView.as_view()),
    path('football/news/<int:pk>/', views.CurrentPostView.as_view()),

    path('football/events/', views.EventView.as_view()),
    path('football/events/<int:pk>/', views.CurrentEventView.as_view()),

    path('football/events/active', views.CurrentSportEventView.as_view()),
    path('football/events/upcoming', views.CurrentSportEventView.as_view()),
    path('football/events/past', views.CurrentSportEventView.as_view()),
]