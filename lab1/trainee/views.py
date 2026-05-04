from django.shortcuts import render
from django.http.response import HttpResponse

def trainee_list(request):
    return render(request,'trainee/list.html')
def add_trainee(request,name):
    return HttpResponse(f'<h1> Add Trainee name: {name} </h1>')
def update_trainee(request,id):
    return HttpResponse(f'<h1> Update trainee for id {id} </h1>')
def delete_trainee(request,id):
    return HttpResponse(f'<h1> Delete trainee for id {id} </h1>')
