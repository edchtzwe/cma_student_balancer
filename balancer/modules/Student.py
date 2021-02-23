from balancer.models import Student
from balancer.utilities import ReturnQueryPackets
from django.urls import reverse

def GetAllStudents():
    return Student.objects.all()

def GetStudentIndexContext(kwargs):
    page_record_size = int(kwargs['limit'])
    page = int(kwargs['page'])

    all_students = GetAllStudents()
    num_students = len(all_students)
    query_packet = ReturnQueryPackets(all_students, page_record_size)
    num_pages = len(query_packet) - 1

    # snap to the last page if they're navigating out of bounds
    if page > num_pages:
        page = num_pages

    # get paginated queryset
    paginated_queryset = query_packet.get(str(page))

    # navigation operations
    prev_link = ''
    next_link = ''
    # if the navigated page is the last page
    if page == num_pages:
        prev_link = str(page - 1)
    # if we are at the beginning
    elif page == 0:
        next_link = str(page + 1)
    # we are in the middle
    else:
        prev_link = str(page - 1)
        next_link = str(page + 1)

    context={
        'num_students'       :num_students,
        'all_students'       :all_students,
        'paginated_querys et':paginated_queryset,
        'paginated_queryset' :paginated_queryset,
        'prev_link'          :prev_link,
        'next_link'          :next_link,
        'filter_form_action' :reverse('student-find'),
    }
    return context