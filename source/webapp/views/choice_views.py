from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from webapp.models import Poll,Choice
from webapp.forms import PoolForm,ChoiceForm


class CreateChoice(CreateView):
    model = Choice
    form_class = ChoiceForm

    def form_valid(self, form):
        pool = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        pool.choices.create(text=form.cleaned_data['text'], poll_choice=choice)
        pool.save()
        return redirect('watch_poll', pool.pk)

    def get_success_url(self):
        return reverse('watch_poll', kwargs={'pk': self.object.pk})


class EditChoice(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name ='Choices/choice_update.html'

    def get_success_url(self):
        return reverse('watch_poll', kwargs={'pk': self.object.pk})


class DeleteChoice(DeleteView):
    template_name = 'Choices/choice_delete.html'
    model = Choice

    def get_success_url(self):
        return reverse('watch_poll', kwargs={'pk':self.object.poll_choice.pk})