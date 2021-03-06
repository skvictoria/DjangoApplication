from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
import os
from django.http import HttpResponse

def test(request):
    context={'key': 'value',
             'list_1':[[10,20,"list"],[20,10]]
             }
    print("test")
    print(request.POST.get('id'))
    return render(request, 'HTML/start.html', context)
    
def upload(request):
    if request.method=='POST':
        for x in request.FILES.getlist("files"):
            uploadFile = open(settings.SAVE_ROOT+"\\"+str(x),"wb")
            for chunk in x.chunks():
                print(chunk)
                uploadFile.write(chunk)
        return redirect("HTML/test.html")
    return render(request, "HTML/test.html")

def download(request, filename):
    path = filename ##임의의 이미지 이름
    file_path = os.path.join(setting.SAVE_ROOT, path)
    if os.path.exists(file_path):
        readFile=open(file_path, "rb")
        response = HttpResponse(readFile.read())
        response['Content-Disposition']='attachment;filename='+os.path.basename(file_path)
        response['Content-type']='application/vnd.ms-excel'#처리해야할 파일이 엑셀파일일 경우
        response['Content-type']='image/png' # 처리해야 할 파일이 이미지파일일 경우
        return response
    
def second(request):
    return render(request, "HTML/info.html")

def mainIndex(request):
    return render(request, "HTML/main.html")

def createAccount(request):
    if request.method =='POST':
        User.objects.create_user(username=request.POST.get("id"),
                                  password=request.POST.get('pwd'), 
                                  email=request.POST.get('email'))
        #User.objects.get(id=userid)
        #User.objects.all()
        #User.objects.values('id', 'username')
        return redirect('login') 
    else:
        return render(request, "HTML/register.html")
    
def img(request):
    return render(request, "img.html")