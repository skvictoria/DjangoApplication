from django.shortcuts import render, redirect
from phonebook.models import PhoneBook

# Create your views here.
def helloworld(request):
    alluser = PhoneBook.objects.values('id','name','tele')
    print(alluser)
    context = {"phonebook":alluser}
    return render(request, "PBOOK/test.html", context)

def detail(request, userid):
    alluser = PhoneBook.objects.values('id','name','tele','birth', 'writer').get(id=userid)
    ################################################################
    #PhoneBook.objects.values(value, value, ...) #모든 값들 가져옴
    #PhoneBook.objects.get(id=userid) #id가 같은 정보들 모두 가져옴 -> update/delete할 때 쓰임
    #PhoneBook.objects.all() #저장되어 있는 모든 정보들
    #PhoneBook.objects.filter(name='a') #이름이 a인 데이터 모두
    #PhoneBook.objects.exclude(name='a') #이름이 a가 아닌 데이터 모두
    #PhoneBook.objects.count() #row의 총 개수 얻어옴
    #PhoneBook.objects.order_by('-id') #역순(최신글이 위로)
    #################################################################
    context={"phonebook": alluser}
    return render(request, "PBOOK/detail.html", context)


def add(request):
    if request.user.is_active == False:
        return redirect('login')
    if request.method=='POST':
        #print("name :"+request.POST.get('name'))
        table = PhoneBook()
        table.name = request.POST.get('name')
        table.tele = request.POST.get('phNum')
        table.email = request.POST.get('email')
        table.addr = request.POST.get('addr')
        table.birth = request.POST.get('bir')
        table.writer = request.user.username
        table.save() ##데이터베이스에 저장하겠다!
        return redirect("PB:test")
        
    else:
        #get방식으로 가져왔을 때   
        return render(request, "PBOOK/add.html")
    
def update(request, userid):    
    userinfo = PhoneBook.objects.get(id = userid)
    context = {"phonebook": userinfo}
    if request.method=='POST':
        userinfo.name = request.POST.get('name')
        userinfo.tele = request.POST.get('phNum')
        userinfo.email = request.POST.get('email')
        userinfo.addr = request.POST.get('addr')
        userinfo.birth = request.POST.get('bir')
        userinfo.save() ##데이터베이스에 저장하겠다!
        return redirect("PB:test")
    else:
        return render(request, "PBOOK/update.html", context)

def delete(request, userid):
    user = PhoneBook.objects.get(id=userid)
    user.delete()
    return redirect("PB:test")