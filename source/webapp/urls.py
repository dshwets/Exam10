from django.urls import path

from webapp.views.MessagesCreateView import MessageCreateView
from webapp.views.UsersView import UserListView

app_name = 'webapp'


urlpatterns = [
        path('', UserListView.as_view(), name='index'),
        path('send/message/<int:pk>/', MessageCreateView.as_view(), name='send_message')

]
