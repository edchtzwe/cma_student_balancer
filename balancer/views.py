# Django imports
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
# model imports
from balancer.models import Student
from balancer.forms import StudentForm, StudentModifyForm
# python imports
import sys
import re
########################################
########################################
# utility functions
def IsEmpty(p_string):
    # at least one non-space character
    if not re.search("\S+", str(p_string)):
        return True
    return False;

def ModelObjToPyDict(p_model_object):
    py_dict = dict()
    model_fields = p_model_object.get_iterable_fields()

    for field in model_fields:
        py_dict[field] = getattr(p_model_object, field)
    return py_dict

def IsNumber(p_value):
    if re.search("\d+\.?\d*", str(p_value)):
        return True
    return False;
########################################
# views
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
########################################
def index_plus(request, result):
    all_students = Student.objects.all()
    num_students = len(all_students)

    result_info = ''

    ERROR_DICT = {
        'student-delete-success': 'Student successfully deleted',
        'student-modform-error' : 'Student successfully deleted',
    }

    if not IsEmpty(ERROR_DICT[result.lower()]):
        result_info = ERROR_DICT[result.lower()]

    if IsEmpty(result_info):
        result_info = "Something went wrong when constructing the feedback message. Please contact your system administrator to troubleshoot this issue. Please check that your last actions actually took place."

    return render(
        request,
        'index.html',
        context={
        'num_students':num_students,
        'all_students':all_students,
        'result_info' :result_info,
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
                'created_by'  :'edmundsuperadmin',
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
def StudentModifyView(request, pk):
    form = None
    student_object = None

    if not IsEmpty(pk):
        form = StudentModifyForm(initial={'new_balance': 0.0})
        student_object = Student.objects.get(pk=pk)
    else:
        return index_plus(request, 'student-modform-error')
    context = {
        'form': form,
        'pk':pk,
        'student':student_object
    }
    return render(request, 'balancer/student_detail.html', context)
########################################
def StudentDelete(request, student_obj):
    if not re.search("\S+", str(student_obj.pk)):
        return False
    else:
        student_obj.delete()
        return True
########################################
def StudentCommitModify(request, student_obj):
    print('test')
    if not re.search("\S+", str(student_obj.pk)):
        return False
    else:
        new_balance = request.POST['new_balance']
        if not IsEmpty(new_balance) and IsNumber(new_balance):
            # consider using a form class to build our modify form
            # form = RenewBookForm(request.POST)
            student_obj.balance = student_obj.balance + float(new_balance)
            student_obj.balance = round(float(student_obj.balance), 2)
            student_obj.save()
        return True
########################################
def StudentModifyDelete(request):
    if request.method == 'POST':
        student_obj = None

        if 'student-id' in request.POST:
            student_obj = Student.objects.get(pk=request.POST['student-id'])
        if student_obj:
            if 'delete' in request.POST:
                if StudentDelete(request, student_obj):
                    return index_plus(request, 'student-delete-success')
            elif 'modify' in request.POST:
                if StudentCommitModify(request, student_obj):
                    return HttpResponseRedirect( reverse('student-detail', args=[str(student_obj.pk)]) )

    return HttpResponseRedirect( reverse('index') )