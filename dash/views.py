from django.shortcuts import render

# from django.views.generi

# from django.views.generic import ListView, DetailViews
from django.views import generic
from dash.models import post,Comment,category
from django.urls import reverse_lazy
from .forms import  PostForm,EditForm

# Create your views here.


def sam():
    print('welll')



class Bloglistview(generic.ListView):
    model = post
    template_name = 'index.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kargs):
        cats_menu = category.objects.all()
                # why we use all is because it just one item on the model
        context = super(Bloglistview, self).get_context_data(*args, **kargs)
        context['cats_menu'] = cats_menu
        return context


    def sam(self):
        samw = print('sdhdfhdfjh')
        return samw


class Blogdetail(generic.DetailView):

    model =post
    template_name = 'detail.html'

class Createtview(generic.CreateView):

    model = post
    form_class = PostForm
    template_name = 'post.html'
    # fields = ['title','body']

def CategoryView(request, cats):
    category_post = post.objects.filter(category=cats.replace('-', ' ') )
    cats_menu = category.objects.all()
    context = {
            'cats': cats.title(),
            'category_post':category_post,
            'cats_menu':cats_menu,

    }
    return render(request, 'category.html', context)



class AddCategoryView(generic.CreateView):

    model = category
    # form_class = PostForm
    template_name = 'addcategory.html'
    fields = '__all__'

class updatetview(generic.UpdateView):
    model = post
    form_class = EditForm
    template_name = 'edit.html'


class deleteview(generic.DeleteView):
    model = post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

class AddcommentViews(generic.CreateView):
    model = Comment
    template_name = 'add_Comment.html'
    fields = '__all__'

