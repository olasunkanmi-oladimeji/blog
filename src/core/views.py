from django.shortcuts import render,get_object_or_404,redirect,redirect
from core.models import Post,Comment,Contact,Category
from core.forms import CommentForm, PostForm,UpdateForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
class draftView(generic.ListView):
    model = Post
    template_name = 'core/post_list.html'
    ordering = ['-publish_date']

    def get_context_data(self, **kwargs):
        cats=Category.objects.all()
        context = super(draftView, self).get_context_data()
        context['cats'] = cats
        return context

def approved_comments(self):
    return self.comments.filter(approved_comment=True)

def approved_post(self):
    return self.publish_date.filter(timezone.now())
    



#class postCreate(generic.CreateView):
    #model = Post
    #form_class =PostForm
    #template_name = 'core/post_create.html'

    #def form_valid(self, form):
        
    #    instance = Post(video=self.request.FILES['video'])
        
    #    instance.save()

def postCreate(request): 
     
    if request.method == "POST": 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.image = request.FILES.get('image')
            post.video = request.FILES.get('video')
            
            
            post.save()
            return redirect("core:post", pk=post.pk)
    else: 
        form = PostForm()
    return render(request, "core/post_create.html", {"form": form})

class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('core:draft')
    template_name = 'core/post_delete.html'

class PostUpdate(generic.UpdateView):
    model = Post
    form_class = UpdateForm

    template_name = 'core/post_update.html'

@login_required
def post_approve(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.approve_post()
    return redirect('core:post', pk=post.pk)

def homeview(request):
    cats=Category.objects.all()
    post =Post.objects.order_by('-publish_date').filter(publish_date__lt=timezone.now())
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'core/index.html',{'posts':posts,'cats':cats})

def aboutview(request):
    cats=Category.objects.all()

    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # does nothing, just trigger the validation
    else:
        form = ContactForm()

    return render(request,'core/about.html',{'cats':cats,'form':form})

def postview(request,pk):
    cats=Category.objects.all()
    post = get_object_or_404(Post,pk=pk)
    return render(request,'core/post.html',{'post':post,'cats':cats})

def categoryview(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Post.objects.all()

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        cats = items.filter(category=category)
    
    return render(request, 'core/category.html',{'cats' : categories,
                                            'category':category,
                                            'cat':cats} )

def add_comment_to_post(request, pk):
    cats=Category.objects.all()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('core:post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'core/commentpost.html', {'form': form,'cats':cats})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('core:post', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('core:post', pk=comment.post.pk)