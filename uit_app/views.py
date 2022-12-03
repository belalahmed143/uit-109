from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    s_data = Student.objects.all().order_by('?')[:2]
    f_data = Student.objects.filter(roll=9233,name='Mohammad Belal Hossain').order_by('-id')

    t_data = Teacher.objects.all()
    tf_data = Teacher.objects.filter(department__name='EEE')

    context = {
        's_data':s_data,
        'f_data':f_data,
        't_data':t_data,
        # 'tf_data':tf_data,
    }
    return render(request, 'index.html',context)

def about_us(request):
    return render(request, 'about.html')

def contact(request):
    contact_data = Contact.objects.all()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()           
            return redirect('contact')
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form':contact_form, 'contact_data':contact_data})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.email = request.POST.get('email')
            form.save()
            return redirect('home-page')
    return render(request, 'newsletter.html')


def student_add(request):
    if request.method == 'POST':
        student_form = StudentAddForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            return redirect('student-add')
    else:
        student_form = StudentAddForm()
    return render(request, 'student-add.html', {'student_form':student_form})

def student_update(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student_form = StudentAddForm(request.POST, request.FILES, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student-detail', student.pk)
    else:
        student_form = StudentAddForm(instance=student)
    return render(request, 'student-add.html', {'student_form':student_form})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    context = {
        'student':student
    }
    return render(request, 'student-detail.html', context)

def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('/')
    return render(request, 'student-delete.html', {'student':student})





from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy

class TeacherList(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teacher.html'

class TeacherDetail(DetailView):
    model = Teacher
    template_name = 'teacher-detail.html'

class TeacherAdd(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('teacher-add')

class TeacherUpdate(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('teacher')

class TeacherDelete(DeleteView):
    model = Teacher
    template_name = 'teacher-delete.html'
    success_url = reverse_lazy('teacher')
    
    




# views.py

# from django.views.generic import DeleteView
# from django.urls import reverse_lazy

# class TeacherDelete(DeleteView):
#     model = Teacher
#     template_name = 'teacher-delete.html'
#     success_url = reverse_lazy('teacher')

# urls.py

# path('teacher/<pk>/information/delete', TeacherDelete.as_view(), name='teacher-delete'),

# delete.html

# <div class="container my-5">
#     <h4 class="text-center">Teacher Delete</h4>
#     <div class="col-11 col-md-6 mx-auto shadow">
#         <form class="p-3" action="" method="POST">
#             {% csrf_token %}    
#             <button class="btn btn-primary col-12" type="submit">Are You sure ! delete this profile</button>
#         </form>

#     </div>
# </div>
    