from django.urls import path

from . import views

urlpatterns = [
     path('student-dashboard/', views.student_dashboard, name="student-dashboard"),
     
     path('create-article2', views.create_article, name="create-article2"),

     path('browse-articles', views.browse_articles, name="browse-articles"),
     
     path('my-articles2', views.my_articles, name = "my-articles2"),

     path('update-article2/<str:pk>', views.update_article, name="update-article2"),

     path('delete-article2/<str:pk>', views.delete_article, name="delete-article2"),

     path('account-management3', views.account_management, name='account-management3'),

     path('delete-account2', views.delete_account, name='delete-account2'),



]