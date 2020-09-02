from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView,View

from webapp.models import Poll,Choice,Answer
from webapp.forms import PoolForm,ChoiceForm


class CreateAnswer(View):
    template_name ='Answers/answer_create.html'

    def get(self,request,*args,**kwargs):
        context = {}
        context['poll'] = Poll.objects.get(pk=self.kwargs['pk'])
        context['choices'] = context['poll'].choices.all()
        return render(request, self.template_name,context=context)

    def post(self,request,*args,**kwargs):
        pool = Poll.objects.get(pk=kwargs['pk'])
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=int(choice_id))
        Answer.objects.create(pool=pool, choice=choice)
        return redirect('main_page')


# def get_context_data(self, **kwargs):
#     print(self.kwargs)
#     context = super().get_context_data()
#     context['poll'] = Poll.objects.get(pk=self.kwargs['pk'])
#     context['choices'] = context['poll'].choices.all()
#     print(context['choices'])
#     # context['choices']
#     return context