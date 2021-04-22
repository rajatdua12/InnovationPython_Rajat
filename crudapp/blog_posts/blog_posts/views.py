from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from blog_posts.models import CrudApp

class CrudAppForm(ModelForm):
    class Meta:
        model = CrudApp
        fields = "__all__"

def post_list(request, template_name='blog_posts/post_list.html'):
    post = CrudApp.objects.all()
    data = {}
    data['object_list'] = post
    print(post)
    return render(request, template_name, data)

def post_create(request, template_name='blog_posts/post_form.html'):
    form = CrudAppForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form':form})

def post_update(request, pk, template_name='blog_posts/post_form.html'):
    post = get_object_or_404(CrudApp, pk = pk)
    form = CrudAppForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form':form})

def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
    post = get_object_or_404(CrudApp, pk = pk)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, template_name, {'object':post})
