from django.contrib import admin

from apps.storage.models import FileUpload, Directory, Download


class FileUploadInline(admin.StackedInline):
    model = FileUpload
    fields = ('id', 'file', 'timestamp', 'owner')
    readonly_fields = ('id', 'file', 'timestamp', 'owner')
    verbose_name = 'File'
    verbose_name_plural = 'Files'
    extra = 0


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    search_fields = ('file',)
    list_display_links = ('file',)
    list_display = ('id', 'file', 'timestamp', 'owner')


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
