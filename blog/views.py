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
    
def post_detail(request, post_id,post):
    #post = get_object_or_404(Post,pk=pk,status='published')
   
    
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
                  'blog/post/post_detail.html',
                 {'post': Post.objects.get(id=post_id),
                  'comments': comments,
                  'comment_form': comment_form})
    

