from django.urls import path

from webapp.views.UsersView import UserListView

app_name = 'webapp'


urlpatterns = [
        path('', UserListView.as_view(), name='index'),

]
