from core import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('',views.homeview,name='home'),
    path('about',views.aboutview,name='about'),
    path('category/<slug:category_slug>',views.categoryview,name='category'),
    path('post/<pk>',views.postview,name='post'),
    path('publish/post/<int:pk>',views.post_approve,name='post_approve'),
    path('new/post',views.postCreate,name='postCreate'),
    path('draft',views.draftView.as_view(),name='draft'),
    path('delete/post/<int:pk>',views.PostDelete.as_view(),name='PostDelete'),
    path('Post/Update/<int:pk>',views.PostUpdate.as_view(),name='PostUpdate'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)