from django.urls import path

from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path('add', views.add_event, name='add_event'),  # 120.0.0.1:8000/events/add
    path('<int:pk>', views.event_detail, name='event_detail'),  # 127.0.0.1:8000/events/PyCon
    # path('<str:name>', views.Speaker_Details, name='Speaker_Detail'), # 127.0.0.1:8000/events/PyCon
]
