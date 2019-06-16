
from django.urls import include, path
from . import views

app_name = 'polls'
urlpatterns = [

    # ex: /polls/
    path('', views.index, name='index'),
    path('generatequotes', views.generatequotes, name='generatequotes'),

    # ex: /polls/5/
    path('find', views.detail, name='find'),
    path('best', views.getbest, name='best'),
    path('database', views.database, name='database'),
    path('getname', views.get_name, name='get_name'),
    path('<int:question_id>/', views.info, name='detail'),
    path('<int:question_id>/add', views.add, name='add'),
#path('bobr',ve, name='
    ]

