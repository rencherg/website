from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

from .models import Comment
from django.utils import timezone

from .forms import CommentForm

# Create your views here.

def index(request):
    comment_list = Comment.objects.order_by('-pub_date')
    context = {'comment_list': comment_list}
    
    return render(request, 'forum/index.html', context)
    
def comment(request, comment_id):
    try:
        c = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")
    return render(request, 'forum/comment.html', {'comment': c})
    
def new_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('/forum/')
    else:
        form = CommentForm()
    return render(request, 'forum/new_comment.html', {'form': form})
