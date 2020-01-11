from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$',views.homepage.as_view(),name='homepage'),
    url(r'About us$',views.aboutview.as_view(),name='about'),
    url(r'New Post$',views.newpost.as_view(),name='newpost'),
    url(r'^Post/(?P<pk>\d+)/$',views.postdetail.as_view(),name='postdetail'),
    url(r'blog/list$',views.draft.as_view(),name='draft'),
    url(r'Post/update/(?P<pk>\d+)$',views.UpdateView.as_view(),name='update'),
    url(r'Post/delete/(?P<pk>\d+)$',views.DeleteView.as_view(),name='delete'),
    url('post/(?P<pk>\d+)/comment/$', views.add_comment_to_post,name='add_comment_to_post'),
    url('comment/(?P<pk>\d+)/approve/', views.comment_approve, name='comment_approve'),
    url('comment/(?P<pk>\d+)/remove/', views.comment_remove, name='comment_remove'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)