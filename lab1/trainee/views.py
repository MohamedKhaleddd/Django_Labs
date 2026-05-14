from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import *
from course.models import *
from .forms import *
from django.views import View
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class Traineelist(LoginRequiredMixin,ListView):
    queryset= Trainee.objects.filter(is_active=True)
    model=Trainee
    template_name='trainee/list.html'
    context_object_name='trainees'
    

@login_required
def trainee_list(request):
    request.session.clear()

    context = {
        'title': 'Tracking',
        'trainees': Trainee.objects.filter(is_active=True)
    }

    return render(request, 'trainee/list.html', context)

@login_required
def gettraineebyid(request, id):

    context = {
        'trainee': Trainee.objects.get(id=id)
    }

    return render(request, 'trainee/traineedetails.html', context)

@login_required
def update_trainee(request, id):
    oldtrainee=Trainee.objects.get(pk=id)
    if request.method=='POST':
        form=TraineeFormModel(data=request.POST,files=request.FILES,instance=oldtrainee)
        if form.is_valid():
            form.save()
        else:
                return render(request,'trainee/update.html',{'form':form,'errors':form.errors})



    return render(request,'trainee/update.html',{'form':TraineeFormModel(instance=oldtrainee)})



@login_required
def softdelete(request,id):
    Trainee.objects.filter(pk=id).update(is_active=False)
    return redirect('Traineelist')



@login_required
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
    request.session['info']="Trainee Added"
    return render(request, 'trainee/new.html',context)



@login_required
def getTraineebyname(request, name):

    objresponse = HttpResponse(
        f'<h1> Get Trainee by name : {name} </h1>'
    )

    objresponse.write('added response')

    return objresponse



@login_required
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