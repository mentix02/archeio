import os
import uuid

from django.db import models
from django.db.models.functions import Now


class Directory(models.Model):

    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(db_default=Now(), editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='directories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subdirectories', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Directory'
        verbose_name_plural = 'Directories'


class FileUpload(models.Model):

    DOWNLOADS_COUNT_ANNOTATION = 'download_count'

    file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField(db_default=Now(), editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='uploads')
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='files', null=True, blank=True)

    @property
    def download_count(self) -> int:
        if hasattr(self, self.DOWNLOADS_COUNT_ANNOTATION):
            return getattr(self, self.DOWNLOADS_COUNT_ANNOTATION)
        return self.downloads.count()

    def __str__(self) -> str:
        return os.path.basename(self.file.name)

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'File Upload'
        verbose_name_plural = 'File Uploads'


class Download(models.Model):

    timestamp = models.DateTimeField(db_default=Now(), editable=False)
    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE, related_name='downloads')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='downloads')
