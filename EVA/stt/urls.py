from django.urls import path
from . import views

app_name = "stt"
urlpatterns = [
    path("", views.index, name="stt_index"),
    path('upload/', views.upload_audio, name='upload_audio'),
    path('result_json/<int:identifier>/', views.result_json, name='result_json')
]
