from .models import Teacher

def eee_teacher(request):
    tf_data = Teacher.objects.filter(department__name='EEE')
    context = {
        'tf_data':tf_data
    }
    return context