
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from . import models
from . import forms

def blogs(request):
    return render(request, 'blogs.html')


def index(request):
    all_posts = models.Posts.objects.all()
    return render(request, 'index.html', {'posts': all_posts})


def show(request, post_id):
    # thepost = models.Posts.objects.get(id=post_id)
    thepost = get_object_or_404(models.Posts, id=post_id)
    return render(request, 'show.html', {'post': thepost})


def create(request):
    
    if request.method == 'POST':
        details = forms.InputForm(request.POST)
        
        if details.is_valid():
            title = details.cleaned_data.get('title', '')
            body = details.cleaned_data.get('body', '')
            newpost = models.Posts(title=title, body=body)
            newpost.save()
            messages.success(request,"Post created successfull")
            theform = forms.InputForm()
            return render(request,'create.html',{'form':theform})
        else:
            return render(request,'create.html',{'form':details})
        
        
    theform = forms.InputForm()
    return render(request, 'create.html',{'form':theform})


def store(request):
    # if request.method == 'POST':
    #     title = request.POST.get('title', '')
    #     body = request.POST.get('body', '')
    #     # newpost = models.Posts(title=title, body=body)
    #     # newpost.save()
    #     messages.success(request, "Post created successfull")
    #     return redirect('post_create')

    if request.method == 'POST':
        details = forms.InputForm(request.POST)
        
        if details.is_valid():
            title = details.cleaned_data.get('title', '')
            body = details.cleaned_data.get('body', '')
            newpost = models.Posts(title=title, body=body)
            newpost.save()
            messages.success(request,"Post created successfull")
            return render(request,'create.html')
        else:
            return render(request,'create.html',{'form':details})

    # if request.method == 'POST':
    #     newform = forms.InputFormModel(request.POST or None)

    #     if newform.is_valid():
    #         newform.save()
    return render(request, 'create.html')

def update(request):
    pass


def modss(request):
    # b1 = models.Posts()
    # b1.title = 'This is second three'
    # b1.body = 'This is the three body Some quick example text to build on the card title and make up the bulk of the card content. '
    # b1.save()

    all_entries = models.Posts.objects.all()

    for x in all_entries:

        print(x.title)

    return HttpResponse('success')


