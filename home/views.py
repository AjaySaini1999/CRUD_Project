from django.shortcuts import render, redirect
from .models import Student
from django.views import View
from .forms import Add_stu
# Create your views here.


def index(request):
    stu_data = Student.objects.all()
    return render(request, 'home.html', {'stu_data': stu_data})


def add_stu(request):
    fm = Add_stu()
    fs = Add_stu(request.POST)
    if fs.is_valid():
        fs.save()
        return redirect('/')
    return render(request, 'add_stu.html', {'fm': fm})


def del_stu(request):
    data = request.POST.get('id')
    studata = Student.objects.get(id=data)
    studata.delete()
    return redirect('/')


def edit_stu(request, id):
    stu = Student.objects.get(id=id)
    # fm = Add_stu(instance=stu)
    fn = Student.objects.get(request.POST, instance=stu)
    if fn.is_valid:
        fn.save()
        return redirect('/')

    return render(request, 'edit_stu.html')


class Edit_stu(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = Add_stu(instance=stu)

        return render(request, 'edit_stu.html', {'fm': fm})

    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fn = Add_stu(request.POST, instance=stu)
        if fn.is_valid:
            fn.save()
            return redirect('/')
