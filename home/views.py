from django.shortcuts import redirect, render
from home.models import Url

def create(req) :
    if req.method=="POST" :
        full_url=(req.POST.get('full_url'))
        obj=Url.create(full_url)
        return render(req, 'homes/index.html',{
            'full_url' : obj.full_url,
            'short_url'  : req.get_host()+'/'+obj.short_url
        })

    return render(req, 'homes/index.html')
   
# Create your views here.

def routetourl(req, key) : 
    try : 
        obj=Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except : 
        return redirect(create)
  