from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm, SearchForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.files.storage import default_storage
import os
# Create your views here.
def tweet(request):
    return render(request, 'tweet.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        old_photo= tweet.photo if tweet.photo else None
        if form.is_valid():
            if 'photo' in request.FILES and old_photo:
                # Delete the old photo if it exists
                    default_storage.delete(old_photo.name)
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})


def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":

        if tweet.photo:
            default_storage.delete(tweet.photo.name)
        tweet.delete()
        return redirect('tweet_list')
    return render (request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()

    return render(request, 'Registration/register.html',{'form':form})

def search(request):
    query = request.POST.get('q')  # Get the search term from the POST request
    if query:
        tweets = Tweet.objects.filter(text__icontains=query).order_by('-created_at')  # Filter tweets containing the search term
    else:
        tweets = Tweet.objects.all().order_by('-created_at')  # If no search term, return all tweets
    
    return render(request, 'tweet_list.html', {'tweets': tweets})   