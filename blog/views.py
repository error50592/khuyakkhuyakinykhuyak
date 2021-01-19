from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import  CommentForm
def post_list(request):
    object_list = Post.objects.all() #published
    paginator = Paginator(object_list, 3)  
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
      
        posts = paginator.page(1)
    except EmptyPage:
        
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/home.html',
                  {'page': page ,
                   'posts': posts})
    posts = Post.published.all()
    return render(request, 'blog/post/home.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'blog/post/post_detail.html', {'post': post})
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
           
            new_comment = comment_form.save(commit=False)
         
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})

'''
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Post,Comment
from .forms import CommentForm
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    comments = Post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'blog/post/post_detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})

def index(request):
	return render(request,'about.html')
'''