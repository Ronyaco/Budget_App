from django.urls import reverse_lazy , reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView

from my_finances.forms import IncomeForm
from my_finances.models import Income

class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    #template_name = 'my_finances_list.html'



class IncomeDetailView(DetailView):
    model = Income

class IncomeCreateView(CreateView):
    model = Income
    #form_class = IncomeForm
    success_url = reverse_lazy('my_finances:income_list')
    def get_form_class(self):
        if 'default' in self.request.GET:
            self.fields = ['value', 'date', 'name']
            return super().get_form_class()
        else:
            return IncomeForm

    #template_name = 'my_finances/income_form'

    def get_success_url(self):
        messages.success(self.request, "Income created successfully")
        return reverse_lazy('my_finances:income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm

    def get_success_url(self):
        messages.success(self.request, "Income updated successfully")
        return reverse('my_finances:income_detail', kwargs={'pk': self.object.pk} ) 


class IncomeDeleteView(SuccessMessageMixin,  DeleteView):
    model = Income
    success_url = reverse_lazy('my_finances:income_list')
    success_message = "It was created successfully"
