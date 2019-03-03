from django.shortcuts import render
from balancer.models import Student
from django.views import generic

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

class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        return context