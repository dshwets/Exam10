from django.urls import path

from webapp.views.Messages import MessageCreateView, SendedMessages, RecivedMessages
from webapp.views.UsersView import UserListView

app_name = 'webapp'


urlpatterns = [
        path('', UserListView.as_view(), name='index'),
        path('send/message/<int:pk>/', MessageCreateView.as_view(), name='send_message'),
        path('messages/sended', SendedMessages.as_view(), name='sended_message'),
        path('messages/recived', RecivedMessages.as_view(), name='recived_message'),

]
