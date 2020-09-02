from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from webapp.models import Poll,Choice,Answer
from webapp.forms import PoolForm, ChoiceForm

class IndexView(ListView):
    model = Poll
    template_name ='Poll/index.html'
    paginate_by = 5
    paginate_orphans = 0
    ordering = ['-created_at']


class WatchPool(DetailView):
    model = Poll
    template_name = 'Poll/watch_pool.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['choices'] = self.object.choices.all
        context['form'] = ChoiceForm
        return context


class UpdatePool(UpdateView):
    model = Poll
    form_class = PoolForm
    template_name = 'Poll/poll_update.html'

    def get_success_url(self):
        return reverse('watch_poll', kwargs={'pk': self.object.pk})


class CreatePool(CreateView):
    model = Poll
    form_class = PoolForm
    template_name = 'Poll/poll_create.html'
    success_url = reverse_lazy('main_page')


class DeletePoll(DeleteView):
    template_name = 'Poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('main_page')