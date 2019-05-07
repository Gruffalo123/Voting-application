from django.urls import path
from polls import views

# 命名空间
app_name = 'polls'

# 使用通用视图 解决冗余问题
urlpatterns = [
    # ex: /polls/
    path('',views.IndexView.as_view(),name='index'),
    # path('index/',views.index,name='index'),# 二级路由 polls/index

    # ex: /polls/5
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    # ex: /polls/5/results
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    # ex : /polls/5/vote
    path('<int:question_id>/vote/',views.vote,name='vote'),
]