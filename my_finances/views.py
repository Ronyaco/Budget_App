from django.urls import reverse_lazy , reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView

from my_finances.forms import IncomeForm , OutcomeForm
from my_finances.models import Income , Outcome

class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    template_name = 'my_finances/income_list.html'
    extra_context = {'title': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=self.request.user).order_by('-date')

    



class IncomeDetailView(DetailView):
    model = Income
    template_name = 'my_finances/income_detail.html'
    extra_context = {'detail_what': 'Income'}


    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=self.request.user).order_by('-date')

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully')
        return reverse('my_finances:income_list')

class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'my_finances/income_form.html'
    success_url = reverse_lazy('my_finances:income_list')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




    def get_form_class(self):
        if 'default' in self.request.GET:
            self.fields = ['value', 'date', 'name']
            return super().get_form_class()
        else:
            return IncomeForm

    

    def get_success_url(self):
        messages.success(self.request, "Income created successfully")
        return reverse_lazy('my_finances:income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'my_finances/income_form.html'

    def get_success_url(self):
        messages.success(self.request, "Income updated successfully")
        return reverse('my_finances:income_detail', kwargs={'pk': self.object.pk} ) 


class IncomeDeleteView(SuccessMessageMixin,  DeleteView):
    model = Income
    success_url = reverse_lazy('my_finances:income_list')
    success_message = "It was created successfully"


class OutcomeListView(ListView):
    model = Outcome
    paginate_by = 100
    template_name = 'my_finances/outcome_list.html'

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=self.request.user).order_by('-date')



class OutcomeDetailView(DetailView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/outcome_detail.html'
    extra_context = {'detail_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=self.request.user).order_by('-date')

class OutcomeCreateView(CreateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/outcome_form.html'
    success_url = reverse_lazy('my_finances:outcome_list')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




    def get_form_class(self):
        if 'default' in self.request.GET:
            self.fields = ['value', 'date', 'name']
            return super().get_form_class()
        else:
            return OutcomeForm



    def get_success_url(self):
        messages.success(self.request, "Outcome created successfully")
        return reverse_lazy('my_finances:outcome_list')


class OutcomeUpdateView(UpdateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/outcome_form.html'

    def get_success_url(self):
        messages.success(self.request, "Outcome updated successfully")
        return reverse('my_finances:outcome_detail', kwargs={'pk': self.object.pk} ) 


class OutcomeDeleteView(SuccessMessageMixin,  DeleteView):
    model = Outcome
    success_url = reverse_lazy('my_finances:outcome_list')
    success_url = reverse_lazy('my_finances:outcome_list')
    success_message = "It was created successfully"