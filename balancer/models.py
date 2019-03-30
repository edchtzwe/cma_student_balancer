from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

class Student(models.Model):
    student_id        = models.CharField(max_length=512)
    # data fields
    first_name        = models.CharField(max_length=256)
    surname           = models.CharField(max_length=256)
    given_name        = models.CharField(max_length=256)
    belt_color        = models.CharField(max_length=256)
    dan_level         = models.IntegerField(blank  =True, null=True)
    balance           = models.FloatField(default  =0.0)

    # audit
    created_by        = models.CharField(max_length=256)
    created_date      = models.DateField()
    last_modified_by  = models.CharField(max_length=256, blank=True, null=True)
    last_modified_date= models.DateField(blank     =True, null=True)
    last_action       = models.CharField(max_length=256, blank=True, null=True)

    # metadata
    class Meta:
        ordering = ['first_name', 'surname']

    # methods
    def __str__(self):
        return ('{0} {1} {2} {3}'.format(self.first_name, self.surname, self.given_name, self.balance))

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.pk)])

    # this should return everything, this needs strict permission controls
    def get_all_fields_as_iterable(self):
        fields = [
            'student_id'        ,
            'first_name'        ,
            'surname'           ,
            'given_name'        ,
            'belt_color'        ,
            'dan_level'         ,
            'balance'           ,
            'created_by'        ,
            'created_date'      ,
            'last_modified_by'  ,
            'last_modified_date',
            'last_action'       ,
        ]
        return fields

    # this will be what's available to most users
    def get_iterable_fields(self):
        fields = [
            'student_id',
            'first_name',
            'surname'   ,
            'given_name',
            'balance'   ,
        ]
        return fields