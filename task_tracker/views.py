from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime, date
from django.utils.decorators import method_decorator



def task_tracker(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_tracker/task_list.html', context)

class TaskCreateView(CreateView):
    model = Task
    fields = ['client_name', 'job_description', 'reoccurring', 'phone_number', 'job_address', 'frequency', 'case_manager', 'contractor', 'assign_to', 'last_booking_date', 'new_booking_date', 'time_confirmed', 'status', 'comments']
    template_name = 'task-create.html'

    def form_valid(self, form):
        # Save the task instance
        self.object = form.save()

        # Return a JSON response
        return JsonResponse({'success': True, 'task_id': self.object.id})

    def form_invalid(self, form):
        # Return a JSON response with errors
        return JsonResponse({'success': False, 'errors': form.errors})

    

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['client_name', 'job_description', 'reoccurring', 'phone_number', 'job_address',
              'frequency', 'case_manager', 'contractor', 'assign_to', 'last_booking_date', 'new_booking_date',
              'time_confirmed', 'status', 'comments']
    success_url = reverse_lazy('task_list')
    template_name = 'task_tracker/task-update.html'

    def form_valid(self, form):
        self.object = form.save()
        data = {
            'success': True,
            'message': 'Task updated successfully'
        }
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {
            'success': False,
            'message': 'Error updating task',
            'errors': form.errors.as_json(),
        }
        return JsonResponse(data)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class TaskListView(ListView):
    model = Task
    template_name = 'task_tracker/task_list.html'
    context_object_name = 'tasks'
    ordering = ['id']
    paginate_by = Task.objects.count()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            tasks = self.get_queryset()
            data['tasks'] = list(tasks.values())
            return JsonResponse(data)
        return super().get(request, *args, **kwargs)




@method_decorator(csrf_exempt, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_tracker:task-list')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return JsonResponse({'success': True})
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return JsonResponse({'success': True})
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UserTaskListView(ListView):
    model = Task
    template_name = 'task_tracker/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Task.objects.filter(author=user).order_by('-id')


class TaskDetailView(DetailView):
    model = Task
    def get_absolute_url(self):
        return reverse('task_tracker:task-detail', args=[str(self.pk)])


class TaskListView(ListView):
    model = Task
    template_name = 'task_tracker/task_list.html'
    context_object_name = 'tasks'
    ordering = ['id']
    paginate_by = Task.objects.count()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            tasks = self.get_queryset()
            data = [{'id': task.id, 'client_name': task.client_name, 'job_description': task.job_description,
                    'reoccurring': task.reoccurring, 'phone_number': task.phone_number,
                    'job_address': task.job_address, 'frequency': task.frequency,
                    'case_manager': task.case_manager, 'contractor': task.contractor,
                    'assign_to': task.assign_to, 'last_booking_date': task.last_booking_date,
                    'new_booking_date': task.new_booking_date, 'time_confirmed': task.time_confirmed,
                    'status': task.status, 'comments': task.comments} for task in tasks]
            return JsonResponse({'success': True, 'data': data})
        return super().get(request, *args, **kwargs)

