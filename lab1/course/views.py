from django.shortcuts import render
from django.http.response import HttpResponse

def course_list(request):
    return HttpResponse('<h1> Course List </h1>')
def add_course(request,name):
    return HttpResponse(f'<h1> Add Course name: {name} </h1>')
def update_course(request,id):
    return HttpResponse(f'<h1> Update course for id {id} </h1>')
def delete_course(request,id):
    return HttpResponse(f'<h1> Delete course for id {id} </h1>')


