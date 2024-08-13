from django.shortcuts import render
from tweet.models import Tweet
def index(request):
    tweets= Tweet.objects.all().order_by('-created_at')
    return render(request, 'home.html',{'tweets':tweets})