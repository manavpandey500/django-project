from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    date = datetime.datetime.now()
    isActive = True
    name = "please click on navigation tabs for further information"
    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
    }
    # return HttpResponse("<h1> Hello This is Index </h1>" + str(date))
    return render(request, "home.html", data)


def personal_details(request):
    date = datetime.datetime.now()
    isActive = True
    name = "please click on navigation tabs for further information"
    student = {
        'student_name': "Manav Pandey",
        'student_college': "ABESIT",
        'student_city': "Ghaziabad"
    }
    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
        'student_data': student
    }
    return render(request, "personaldetails.html", data)


def subjects(request):
    date = datetime.datetime.now()
    isActive = True
    name = "please click on navigation tabs for further information"
    list_of_subject = [
        'Database Management System',
        'Operating System',
        'Data Structures and Algorithm',
        'Computer Networks'
    ]
    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_subject': list_of_subject,
    }
    return render(request, "subjects.html", data)
