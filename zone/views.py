from django.shortcuts import render
from zone.forms import zone_from
from django.http import HttpResponseRedirect
from zone.models import info
# Create your views here.
def zone_def(request):
    if request.method=='POST':
        zon=zone_from(request.POST)
        if zon.is_valid():
            
            fn=zon.cleaned_data['frist_name']
            ln=zon.cleaned_data['last_name']
            em=zon.cleaned_data['email']
            sr=zon.cleaned_data['serial']
            pas=zon.cleaned_data['password']
            rpass=zon.cleaned_data['Repassword']
            tx=zon.cleaned_data['text']
            ck=zon.cleaned_data['chackbox']
            pm=zon.cleaned_data['payment']
            dj=zon.cleaned_data['django']

            harun= info(frist_name=fn,last_name=ln,email=em,serial=sr,password=pas,repassword=rpass,text=tx,chackbox=ck,payment=pm,django=dj) 

            harun.save() 

            return HttpResponseRedirect('/ss/')
        
    else:
        zon=zone_from()
        print('this get')
    return render(request,'zone.html',{'z':zon})

def suc(request):
    return render(request,'ss.html')