from django.shortcuts import render , redirect
from .models import Contact
from .models import student
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
     
    return render(request, 'index.html' , {'students': student.objects.all()})
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you would typically save the data to the database
        # For example:
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, "Contact form submitted successfully.")
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
def add_student(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        # Here you would typically save the data to the database
        # For example:
        student.objects.create(rollno=rollno, name=name, email=email, age=age, address=address)
        messages.success(request, "Student added successfully.")
        return redirect('index')
    return render(request, 'add_student.html')
def delete_student(request, rollno):
    try:
        stud = student.objects.get(rollno=rollno)
        stud.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('index')
    except student.DoesNotExist:
        return render(request, 'index.html', {'error': 'Student not found'})
def update_student(request, rollno):
    try:
        stud = student.objects.get(rollno=rollno)
        if request.method == 'POST':
            stud.name = request.POST.get('name')
            stud.email = request.POST.get('email')
            stud.age = request.POST.get('age')
            stud.address = request.POST.get('address')
            stud.save()
            messages.success(request, "Student updated successfully.")
            return redirect('index')
        return render(request, 'update_student.html', {'student': stud})
    except student.DoesNotExist:
        return render(request, 'index.html', {'error': 'Student not found'})
def search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        # 🔍 Search in Student model
        student_results = Student.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(address__icontains=query) |
            Q(age__icontains=query) |
            Q(rollno__icontains=query)
        )
        results = {
            'students': student_results,
        }
     
    return redirect('index')