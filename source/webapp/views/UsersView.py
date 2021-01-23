from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# from webapp.views.base_view1s import SearchView


class UserListView(ListView):
    model = get_user_model()
    template_name = 'index.html'
    context_object_name = 'users'
    paginate_by = 10
    paginate_orphans = 4

    def get_queryset(self):
        current_query = super().get_queryset().exclude(pk=self.request.user.pk)
        return current_query

