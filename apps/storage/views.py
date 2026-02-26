from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.storage.models import FileUpload
from apps.storage.forms import FileUploadForm
from apps.storage.filters import FileUploadFilter


class FileUploadCreateView(LoginRequiredMixin, CreateView):

    model = FileUpload
    form_class = FileUploadForm
    template_name = 'storage/upload.html'
    success_url = reverse_lazy('storage:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FileUploadListView(LoginRequiredMixin, FilterView):

    paginate_by = 25
    model = FileUpload
    ordering = '-timestamp'
    context_object_name = 'uploads'
    filterset_class = FileUploadFilter
    template_name = 'storage/list.html'

    def get_queryset(self):
        return FileUpload.objects.filter(owner=self.request.user)


class FileUploadDeleteView(LoginRequiredMixin, DeleteView):

    model = FileUpload
    context_object_name = 'upload'
    template_name = 'storage/delete.html'
    success_url = reverse_lazy('storage:list')

    def get_queryset(self):
        return FileUpload.objects.filter(owner=self.request.user)
