from django.urls import path, re_path
from article import views
app_name = 'article'
urlpatterns = [
    # Example: /article/
    path('', views.PostLV.as_view(), name='index'),
    # Example: /article/post/ (same as /article/)
    path('post/', views.PostLV.as_view(), name='post_list'),
    # Example: /article/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    # Example: /article/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    # Example: /article/archive/2020/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    # Example: /article/archive/2020/oct/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    # Example: /article/archive/2019/oct/12/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    # Example: /article/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
    # Example: /article/search/
    path('search/',views.SearchFormView.as_view(),name='search'),

]

