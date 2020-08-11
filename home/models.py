from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secretary = models.BooleanField(default=False)
    ssg = models.BooleanField(default=False)
    perm_sec_political = models.BooleanField(default=False)
    perm_sec = models.BooleanField(default=False)


class File(models.Model):
    file_name = models.CharField(max_length=1000)
    file_number = models.CharField(max_length=100, null=True, blank=True, default=None)
    file = models.FileField()
    date_of_file = models.DateField(null=True, blank=True, default=None)
    comment_from_secretary = models.TextField(max_length=1000, null=True, default=None, blank=True)
    comment_from_ssg = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_by_ssg = models.BooleanField(default=False)
    comment_from_perm_sec1 = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_by_perm_sec1 = models.BooleanField(default=False)
    comment_from_perm_sec2 = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_by_perm_sec2 = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('secretary:append_file_no', kwargs={'file_id': self.pk})

    def __str__(self):
        return self.file_name
# emmamech121@gmail.com
