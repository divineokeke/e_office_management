from django.shortcuts import render, redirect
from django.views.generic import View
from home.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from home.models import File
from django.views import generic
from django.forms.widgets import SelectDateWidget
from django.contrib.auth.models import User


# Create your views here.

def dashboard(request):
    n = 0
    m = 0
    j = 0
    try:
        all_files = File.objects.all()
        for file in all_files:
            if not file.moved_by_ssg:
                n += 1
    except File.DoesNotExit:
        n = 0
    try:
        all_files = File.objects.all()
        for file in all_files:
            if not file.moved_by_perm_sec1 and file.moved_by_ssg:
                m += 1
    except File.DoesNotExit:
        m = 0
    try:
        all_files = File.objects.all()
        for file in all_files:
            if not file.moved_by_perm_sec2 and file.moved_by_ssg and file.moved_by_perm_sec1:
                j += 1
    except File.DoesNotExit:
        j = 0
    context = {'no_of_unread': n, 'perm_sec1_unread': m, 'perm_sec2_unread': j}
    return render(request, 'secretary/s_dashboard.html', context)


class FileIndexView(generic.ListView):
    template_name = 'secretary/history.html'
    context_object_name = 'all_files'

    def get_queryset(self):
        return File.objects.all()


class FileDetailView(generic.DetailView):
    model = File
    template_name = 'home/detail.html'


def s_dashboard(request):
    return render(request, 'secretary/s_dashboard.html')


def upload(request):
    return render(request, "secretary/upload.html")

def comment(request, file_id, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        file = File.objects.get(pk=file_id)
        comment1 = request.POST['comment']
        print(comment1, user.profile.perm_sec_political)
        if user.profile.ssg:
            file.comment_from_ssg = comment1
            file.moved_by_ssg = True
            file.save()
        elif user.profile.perm_sec:
            file.comment_from_perm_sec1 = comment1
            file.moved_by_perm_sec1 = True
            file.save()
        elif user.profile.perm_sec_political:
            print('I am here')
            file.comment_from_perm_sec2 = comment1
            file.moved_by_perm_sec2 = True
            file.save()
        else:
            print('bad')
            return redirect('secretary:s_dashboard')
    return redirect('secretary:s_dashboard')


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(None)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('secretary:s_dashboard'))
        messages.error(request, 'invalid username or password')
        return render(request, self.template_name, {'form': form})


class FileCreate(CreateView):
    model = File
    fields = ['file_name', 'file', 'date_of_file', 'comment_from_secretary']

    def get_form(self, form_class=None):
        form = super(FileCreate, self).get_form()
        form.fields['date_of_file'].widget = SelectDateWidget()
        return form


def append_file_no(request, file_id):
    file = File.objects.get(pk=int(file_id))
    year = file.date_of_file.strftime('%Y')
    file.file_number = 'ssg/' + str(year) + '/' + str(file_id)
    file.save()
    return redirect('secretary:s_dashboard')
