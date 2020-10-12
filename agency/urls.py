from django.urls import path
from agency.views import AgencyLV, AgencyDV


app_name = 'agency'
urlpatterns = [
    path('', AgencyLV.as_view(), name='index'),
    path('<int:pk>/', AgencyDV.as_view(), name='detail'),
]

