from django.urls import path, include

from api.views import FriendsApi
from webapp.views.Messages import MessageCreateView

app_name = 'api'

urlpatterns = [
    path('friends/add/<int:pk>/', FriendsApi.as_view(), name='add_to_friends'),
]
