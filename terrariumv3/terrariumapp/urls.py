from django.urls import path
from . import views

urlpatterns = [
    path('acceuil/', views.index, name='index'),

    path('', views.home, name='home'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add/', views.add, name='add_person'),
    path('person/<int:person_id>', views.display, name='show_person'),
    path('capteurs', views.all_sensor_infos, name='show_sensors'),
    path('capteurs/<str:capteur_type>', views.sensor_infos, name='show_sensor'),
    path('mqtt/<str:action>', views.change_mqtt_client_state, name='show_sensor'),
]