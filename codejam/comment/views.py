from django.shortcuts import render
from django.shortcuts import render_to_response
#from .form import CommentForm
from .models import Comment
# Create your views here.
def comment(request):
	comments=Comment.objects
	return render('comment.html',{'comments':comments})