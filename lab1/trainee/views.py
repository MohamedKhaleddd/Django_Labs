from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import *
from course.models import *
from .forms import *


def trainee_list(request):

    context = {
        'title': 'Tracking',
        'trainees': Trainee.objects.all()
    }

    return render(request, 'trainee/list.html', context)


def gettraineebyid(request, id):

    context = {
        'trainee': Trainee.objects.get(id=id)
    }

    return render(request, 'trainee/traineedetails.html', context)


def update_trainee(request, id):

    return HttpResponse(
        f'<h1> Update Trainee for id {id} </h1>'
    )


def delete_trainee(request, id):

    return HttpResponse(
        f'<h1> Delete Trainee for id {id} </h1>'
    )


def new_Trainee(request):

    if request.method == 'POST':

        form=TraineeFormModel(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Traineelist')
        else:
            context = {'form': TraineeFormModel(request.POST,request.FILES),
                       'error':form.errors}
            return render(request,'trainee/new.html',context)
        


        # Trainee.objects.create(

        #     name=request.POST['name'],
        #     email=request.POST['email'],
        #     phone=request.POST['phone'],
        #     Course=Courses.objects.get(pk=request.POST['courses']),
        #     image=request.FILES['image']
        # )


    context= {'form':TraineeFormModel()}
    return render(request, 'trainee/new.html',context)


def getTraineebyname(request, name):

    objresponse = HttpResponse(
        f'<h1> Get Trainee by name : {name} </h1>'
    )

    objresponse.write('added response')

    return objresponse


def HardTraineeDelete(request, id):

    if Trainee.objects.filter(pk=id):

        Trainee.objects.filter(pk=id).delete()

        return redirect('Traineelist')

    else:

        return render(
            request,
            'trainee/list.html',
            context={'error': 'Trainee not found'}
        )