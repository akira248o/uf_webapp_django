from django.shortcuts import render,redirect
#from django.http import HttpResponse
from .models import Member,Junle,Area
from .forms import MemberForm

## -----------------------------------------
# 最初のページ
## -----------------------------------------
def index(request):
    params = {
        'title': 'Matching Place',
    }
    return render(request,'index.html',params)


## -----------------------------------------
# メンバー登録初期ページ
## -----------------------------------------
def member_register_init(request):
    if(request.method == 'POST'):
        obj = Member()
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/matching_place')
    area_value = Area.objects.all()
    junle_value = Junle.objects.all()
    params = {
        'title': 'Register Member',
        'form': MemberForm(),
        'area_value':area_value,
        'junle_value':junle_value,
    }
    return render(request,'member_register_init.html',params)







def place_register(request):
    params = {
        'title': 'Register Place',
    }
    return render(request,'index.html',params)
