from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import TweetForm

def index(request):
    return render(request, "index.html")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")  # fixed .objects
    return render(request, "tweet_list.html", {"tweets": tweets})
    
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm()  # GET request
    return render(request, "tweet_form.html", {"form": form})
    
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # fixed typo
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)  # fixed
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)  # fixed
    return render(request, "tweet_form.html", {"form": form})
    

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # fixed typo
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_confirm_delete.html", {"tweet": tweet})
