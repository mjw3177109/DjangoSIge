from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
from . import service
def index(request):
    #return HttpResponse('index page')
    poems=service.getAllPoems()
    return  render(request,'poem/index.html',{'poems':poems})
#1.获取数据 通过service模块
#2.render渲染首页


def detail(request,id):
    return HttpResponse("detail page of {}".format(id))


def add(request):
    return HttpResponse("add page")


def delete(request,id):
    return HttpResponse("delete page of {}".format(id))


def edit(request,id):
    return HttpResponse("edit page of {}".format(id))