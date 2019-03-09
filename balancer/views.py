# Django imports
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
# model imports
from balancer.models import Student
from balancer.forms import StudentForm
# python imports
import sys
########################################
########################################
def index(request):
    num_students = Student.objects.all().count()
    all_students = Student.objects.all()

    return render(
        request,
        'index.html',
        context={
        'num_students':num_students,
        'all_students':all_students,
        },
    )
########################################
class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        return context
########################################
def StudentCreate(request):
    form = None

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student_hash = {
                'created_by':'edmundsuperadmin',
                'created_date':"2019-02-17"
            }

            for field in form.cleaned_data:
                student_hash[field] = form.cleaned_data[field]
            record = Student(**student_hash)
            record.save()
            return HttpResponseRedirect(reverse('student-detail', args=[str(record.pk)]) )
    else:
        form = StudentForm(initial={'balance': 0.0})

    context = {
        'form': form,
    }

    return render(request, 'balancer/student_form.html', context)