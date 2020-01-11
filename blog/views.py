from .models import blogpost,commentpost
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import commentform
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
class aboutview(TemplateView):
    template_name = "about.html"

class homepage(ListView):
    model = blogpost
    template_name = "homepage.html"
    context_object_name='list'
    def get_queryset(self):
        return blogpost.objects.order_by('-publish_date').filter(publish_date__lte=timezone.now())
class newpost(CreateView):
    model = blogpost
    template_name = "newpost.html"
    fields='__all__'

class postdetail(DetailView):
    model = blogpost
    template_name = "detail.html"
   
class draft(ListView):
    model = blogpost
    template_name = "draft.html"
    context_object_name='list'
    def get_queryset(self):
        return blogpost.objects.order_by('-created_date').filter(created_date__lte=timezone.now())
class UpdateView(UpdateView):
    model = blogpost
    template_name ="update.html"
    fields='__all__'

class DeleteView(DeleteView):
    model = blogpost
    template_name = "delete.html"
    success_url=reverse_lazy('draft')
  ###############  #######################################
  ##########################
def add_comment_to_post(request, pk):
    post = get_object_or_404(blogpost,pk=pk)
    if request.method == "POST":
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postdetail',post.pk)
    else:
        form = commentform()
    return render(request, 'comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(commentpost,pk=pk)
    comment.approved()
    return redirect('postdetail',comment.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(commentpost, pk=pk)
    comment.delete()
    return redirect('homepage')