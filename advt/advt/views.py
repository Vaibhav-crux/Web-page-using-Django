# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:24:27 2022

@author: Vaibhav Tiwari
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def homePage(request):
    data={
        'title' : 'Home new',
        'bdata':'Welcome to VT',
        'clist':['python','java','django'],
        'numbers':['10','20','30','40','50'],
        'num' : [10,20,30,40,50],
        'student_detail':[
            {'name':'Varun','phone':9564258563},
            {'name':'Dhoni','phone':8654236945}
            ]

        }
    return render(request,"index.html",data)

def submitform(request):
    try:
        if request.method=="POST":
            n1=int(request.POST["num1"])
            n2=int(request.POST["num2"])
            n=n1+n2
            
            return HttpResponse(n)
        
    except:
        pass
def aboutus(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"elements.html",{'output':output})

def forms(request):
    if request.method=="POST":
        if request.Post.get('num1')=="":
            return render(request,"form.html",{'error':True})
        
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        n=n1+n2
        url="elements.html?output={}".format(n)
        return HttpResponseRedirect(url)
        
    return render(request,"form.html")