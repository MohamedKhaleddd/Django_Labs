from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import *


def course_list(request):

    context = {
        'title': 'Tracking',
        'courses': Courses.objects.all()
    }

    return render(request, 'course/list.html', context)


def getcousebycode(request, code):

    context = {
        'course': Courses.objects.get(code=code)
    }

    return render(request, 'course/coursedetails.html', context)


def update_course(request, code):

    return HttpResponse(
        f'<h1> Update course for id {code} </h1>'
    )


def delete_course(request, code):

    return HttpResponse(
        f'<h1> Delete course for id {code} </h1>'
    )


def new_course(request):

    if request.method == 'POST':

        Courses.objects.create(

            name=request.POST['name'],
            description=request.POST['description'],
            tool=request.POST['tool'],
            price=request.POST['price'],
            image=request.POST['image']
        )

        return redirect('Courselist')

    return render(request, 'course/new.html')


def getcoursebyname(request, name):

    objresponse = HttpResponse(
        f'<h1> Get course by name : {name} </h1>'
    )

    objresponse.write('added response')

    return objresponse


def HardCourseDelete(request, code):

    if Courses.objects.filter(pk=code):

        Courses.objects.filter(pk=code).delete()

        return redirect('Courselist')

    else:

        return render(
            request,
            'course/list.html',
            context={'error': 'Course not found'}
        )