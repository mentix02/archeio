import django_filters

from apps.storage.models import FileUpload


class FileUploadFilter(django_filters.FilterSet):

    file = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FileUpload
        fields = ('file', 'timestamp')
