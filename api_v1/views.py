from django.shortcuts import render

# Create your views here.

class manageStudentRecord(RetrieveUpdateDestroyAPIView):
    '''
    This view is used to manage records related to a Student
    '''

    serializer_class = studentSerializer
    lookup_url_kwarg = 'studentId'
    queryset = student.objects.all()


class manageAttendanceRecord(RetrieveUpdateDestroyAPIView):
    '''
    This view is used to manage records related to a Attendance
    '''

    serializer_class = attendanceSerializer
    lookup_url_kwarg = 'id'
    queryset = attendance.objects.all()

class CreateStudent(ListCreateAPIView):
    '''
    This view is used to create a record and retrieve all records to student
    '''

    serializer_class = studentSerializer
    queryset = student.objects.all()
