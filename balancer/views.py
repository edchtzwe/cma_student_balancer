# Django imports
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
# model imports
from balancer.models import Student
from balancer.forms import StudentForm
# python imports
import sys
import re
########################################
########################################
def index(request):
    all_students = Student.objects.all()
    num_students = len(all_students)

    return render(
        request,
        'index.html',
        context={
        'num_students':num_students,
        'all_students':all_students,
        },
    )
    
def index_plus(request, result):
    num_students = Student.objects.all().count()
    all_students = Student.objects.all()

    result_info = ''

    if result.lower() == 'student-delete-success':
        result_info = 'Student successfully deleted'

    if not re.search("\S+", result_info):
        result_info = False

    return render(
        request,
        'index.html',
        context={
        'num_students':num_students,
        'all_students':all_students,
        'result_info':result_info,
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
            return HttpResponseRedirect( reverse('student-detail', args=[str(record.pk)]) )
    else:
        form = StudentForm(initial={'balance': 0.0})

    context = {
        'form': form,
    }

    return render(request, 'balancer/student_form.html', context)
########################################
def StudentDelete(request, student_obj):
    if not re.search("\S+", str(student_obj.pk)):
        return False
    else:
        student_obj.delete()
        return True
########################################
def StudentModifyDelete(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            if 'student-id' in request.POST:
                student_obj = Student.objects.get(pk=request.POST['student-id'])
                if StudentDelete(request, student_obj):
                    return HttpResponseRedirect( reverse('index-plus', args=['student-delete-success']) )
                else:
                    return HttpResponseRedirect( reverse('index-plus', args=['student-delete-fail']) )
    else:
        return HttpResponseRedirect( reverse('index-plus', args=['student-operation-fail']) )

    return HttpResponseRedirect( reverse('index') )