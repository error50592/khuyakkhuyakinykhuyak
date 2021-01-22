from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm
from taggit.models import Tag

def post_list(request, tag_slug=None):
    object_list = Post.objects.all() #published
    paginator = Paginator(object_list, 3)  
    page = request.GET.get('page')
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    #page = request.GET.get('page')

    # ./templates/blog/post/home.html
    return render(request, 'blog/post/home.html', {'page': page , 'posts': posts,'tag': tag})


def post_detail(request, pk):

    template_name = "blog/post/post_detail.html"
    post = get_object_or_404(Post, pk = pk)
    comments = post.comments.filter(active=True).order_by("-created")

    new_comment = None

    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
    # ./templates/blog/post/post_detail.html
def about(request):
    return render(request,'blog/post/about.html')

'''
def post_detail2(request, post_id):
    post = get_object_or_404(Post,pk=pk,status='published')
    comments = ''
    comment_form = ''
   
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
         comment_form = CommentForm(data=request.POST)
         if comment_form.is_valid():
            
             new_comment = comment_form.save(commit=False)
          
             new_comment.post = post
             new_comment.save()
         else:
             comment_form = CommentForm()

    return render(request, 'blog/post/post_detail.html', 
            {'post': Post.objects.get(id=post_id), 
             'comments': comments, 
             'comment_form': comment_form}) 

'''
