from django.urls import path
from . import views

urlpatterns=[ #urls for method based view
             #path('',views.index,name='index'),
             #path('<int:question_id>/',views.detail, name='detail'),
             #path('<int:question_id>/results', views.results,name='results'),
             path('<int:question_id>/vote', views.vote,name='vote'),
              #urls for class based views
             path('',views.Index.as_view(),name='index'),
             path('<int:pk>/',views.Detail.as_view(),name='detail'),
             path('<int:pk>/results/', views.Results.as_view(),name='results')

             ]