from django.views import generic
from django.urls import reverse_lazy
from .models import Greeting
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(generic.ListView):
    template_name = 'greetings/index.html'
    context_object_name = 'greeting_list'

    def get_queryset(self):
        """Return the all greetings."""
        return Greeting.objects.all()


#@login_required(login_url="/accounts/login/")
@method_decorator(login_required, name='dispatch')
class CreateView(generic.edit.CreateView):
    template_name = 'greetings/create.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index') # more robust than hardcoding to /greetings/; directs user to index view after creating a greeting

class ExamplesView(generic.ListView):
    template_name = 'greetings/examples.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'greetings/update.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'greetings/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Greeting
    success_url = reverse_lazy('greetings:index')
