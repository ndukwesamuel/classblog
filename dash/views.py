from django.shortcuts import render

# from django.views.generi

# from django.views.generic import ListView, DetailViews
from django.views import generic
from dash.models import post
from django.urls import reverse_lazy

# Create your views here.


class Bloglistview(generic.ListView):

    model = post
    template_name = 'index.html'
    ordering = ['-id']


class Blogdetail(generic.DetailView):

    model =post
    template_name = 'detail.html'

class Createtview(generic.CreateView):

    model = post

    template_name = 'post.html'
    fields = ['title','aurthor','body']




class updatetview(generic.UpdateView):
    model = post
    template_name = 'edit.html'
    fields = ['title','body']



class deleteview(generic.DeleteView):
    model = post
    template_name = 'deletepost.html'

    success_url = reverse_lazy('home')

