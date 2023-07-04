from django.shortcuts import render , HttpResponse,redirect
from myapp import models
def myapp(request):
    return HttpResponse('Hello,world')


def myapp1(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        models.UserInfo.objects.create(user=username,pwd=password)
        return redirect('/myapp2/')

def myapp2(request):
    user_list=models.UserInfo.objects.all()
    return render(request,'data.html',{'data':user_list})
# Create your views here.
