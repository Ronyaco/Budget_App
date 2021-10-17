from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from my_finances.models import Income

class IncomeListView(ListView):
    model = Income
    paginate_by = 100


class IncomeDetailView(DetailView):
    model = Income




class IncomeCreateView(CreateView):
    model = Income
    fields = ['name','value','date','category','repetitive','repetition_interval','repetition_time','details','user_id']
    success_url = reverse_lazy('my_finances:income_list')

