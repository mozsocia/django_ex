
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from myfirst import models
from myfirst import forms


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
        newform = forms.InputFormModel(request.POST or None)

        if newform.is_valid():
            newform.save()
        else:
            return render(request, 'create.html', {'form': newform})

    theform = forms.InputFormModel()

    return render(request, 'create.html', {'form': theform})


def store(request):
    ''' here is saving data without using form class'''
    # if request.method == 'POST':
    #     title = request.POST.get('title', '')
    #     body = request.POST.get('body', '')
    #     newpost = models.Posts(title=title, body=body)
    #     newpost.save()
    #     messages.success(request, "Post created successfull")
    #     return redirect('post_create')

    ''' here is saving data with normal Form Class the best way '''

    if request.method == 'POST':
        details = forms.InputForm(request.POST)

        if details.is_valid():
            title = details.cleaned_data.get('title', '')
            body = details.cleaned_data.get('body', '')
            newpost = models.Posts(title=title, body=body)
            newpost.save()
            messages.success(request, "Post created successfull")
            theform = forms.InputForm()
            return render(request, 'create.html', {'form': theform})
        else:
            return render(request, 'create.html', {'form': details})

    ''' here is saving data with modeForm '''
    # if request.method == 'POST':
    #     newform = forms.InputFormModel(request.POST or None)

    #     if newform.is_valid():
    #         newform.save()

    return render(request, 'create.html')


def update(request, post_id):

    theOj = models.Posts.objects.get(pk=post_id)

    if request.method == 'POST':
        ''' normal way of update but not recomendeed'''
        # theOj.title = request.POST.get('title', '')
        # theOj.body = request.POST.get('body', '')
        # theOj.save()

        newform = forms.InputFormModel(request.POST, instance=theOj)
        if newform.is_valid():
            newform.save()
            return redirect('post_index')
        else:
            return render(request, 'create.html', {'form': newform, 'pk_id': post_id})

    theform = forms.InputFormModel(instance=theOj)

    return render(request, 'update.html', {'form': theform, 'pk_id': post_id})


def delete(request, post_id):

    theOj = models.Posts.objects.get(pk=post_id)
    theOj.delete()

    # if request.method == 'POST':
    #     theOj.delete()

    return redirect('post_index')


def modss(request):

    # b1 = models.Posts()
    # b1.title = 'This is second three'
    # b1.body = 'This is the three body Some quick example text to build on the card title and make up the bulk of the card content. '
    # b1.save()

    all_entries = models.Posts.objects.all()

    for x in all_entries:

        print(x.title)

    return HttpResponse('success')
