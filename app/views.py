from django.shortcuts import render
from .models import Like
from django.contrib.auth.models import User

# Create your views here.


def index(request):
	like = User.objects.all().count()
	context = {
		'likes':like
	}
	return render(request, 'index.html',context)