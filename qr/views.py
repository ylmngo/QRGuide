from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .models import College, Block, Floor
 
def c_view(request): 
    template = loader.get_template('qr/c.html')
    c = College.objects.get(id=0)
    context  = {
        'c': c, 
        'img': c.img,
    }
    return HttpResponse(template.render(context, request))

def b_view(request, bid): 
    template = loader.get_template('qr/c.html')
    c = College.objects.get(id=0)
    context  = {
        'c': c, 
        'img': c.aimg,
    }
    return HttpResponse(template.render(context, request))

def f_view(request, bid, fid): 
    c = College.objects.get(id=0)
    b = Block.objects.get(id=bid)
    f = Floor.objects.get(id=fid)
    up = False
    down = False
    fu = 0 
    fd = 0  
    if ((fid%10) + 1) <= b.num: 
        up = True
        fu = fid + 1   
    if((fid%10) - 1)  > 0:
        down = True 
        fd   = fid - 1
        print(down) 
    template = loader.get_template('qr/f.html')
    context = {
        'f': f, 
        'img': f.img, 
        'up' : up, 
        'down': down, 
        'fu' : fu,
        'fd' : fd, 
    } 
    return HttpResponse(template.render(context, request)) 

def qr_view(request, bid, fid): 
    c = College.objects.get(id=0)
    b = Block.objects.get(id=bid)
    f = Floor.objects.get(id=fid)
    up = False
    down = False
    fu = 0 
    fd = 0  
    if ((fid%10) + 1) <= b.num: 
        up = True
        fu = fid + 1   
    if((fid%10) - 1)  > 0:
        down = True 
        fd   = fid - 1
        print(down) 
    template = loader.get_template('qr/qr.html')
    context = {
        'f': f, 
        'img': f.aimg, 
        'up' : up, 
        'down': down, 
        'fu' : fu,
        'fd' : fd, 
    } 
    return HttpResponse(template.render(context, request)) 