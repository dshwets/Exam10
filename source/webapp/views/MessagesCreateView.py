# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView


from webapp.forms import MessageForm
from webapp.models import Messages


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'mesage_create.html'
    form_class = MessageForm
    model = Messages

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.reciver = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        message.save()
        return redirect('webapp:index')


    # def get_success_url(self):
    #     return reverse('employees:employee_detail', kwargs={'pk': self.object.pk})