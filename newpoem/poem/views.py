from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from . import service
def index(request):
    #return HttpResponse('index page')
    poems=service.getAllPoems()
    return  render(request,'poem/index.html',{'poems':poems})
#1.获取数据 通过service模块
#2.render渲染首页


def detail(request,id):
    poem =service.getPoem(id)
    #return HttpResponse("detail page of {}".format(id))
    return render(request, 'poem/detail.html', {'poem': poem})


def add(request):
    return render(request,'poem/add.html',{})

def svc_add(request):
    #1.获得form提交的数据 通过post
    #2.将数据提交到数据库
    #3.重定向到首页
    title =request.POST['title']
    content =request.POST['content']
    service.addPoem(title,content)
    return HttpResponseRedirect(reverse('poem:index'))
    #模板中的{% url %} 标签的功能与reverse 一致

def delete(request,id):
    #根据id在数据库中删除诗歌
    #重定向到首页
    service.deletePoem(id)
    return HttpResponseRedirect(reverse('poem:index'))


def edit(request,id):
    ##获取要修改的诗歌
    poem =service.getPoem(id)
    ##渲染修改页面
    return render(request,'poem/edit.html',{'poem': poem})

def svc_edit(request,id):
    #获取修改后的title
    title =request.POST['title']
    content =request.POST['content']
    service.editPoem(id,title,content)
    return HttpResponseRedirect(reverse('poem:index'))