from itertools import count
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from natsort import order_by_index

# ADDED BY ME
from .models import User, Ideas, Comments
from .forms import IdeaForm
import json
from django.utils import timezone
from django.core.paginator import Paginator


def index(request):

    if request.method == "PUT":
        try:
            user = request.user
            data = json.loads(request.body)
            idea = Ideas.objects.get(pk=data.get('id'))
            if data.get("bright") is not None:
                if user not in idea.bright.all():
                    idea.bright.add(user)
                    idea.dark.remove(user)
                    idea.save()
                    ideas = Ideas.objects.order_by('-created')
                    return render(request, "network/index.html", {
                        'ideas': ideas,
                    })
                else:
                    idea.bright.remove(user)
                    idea.save()
                    ideas = Ideas.objects.order_by('-created')
                    return render(request, "network/index.html", {
                        'ideas': ideas,
                    })
            if data.get("dark") is not None:
                if user not in idea.dark.all():
                    idea.dark.add(user)
                    idea.bright.remove(user)
                    idea.save()
                    ideas = Ideas.objects.order_by('-created')
                    return render(request, "network/index.html", {
                        'ideas': ideas,
                    })
                else:
                    idea.dark.remove(user)
                    idea.save()
                    ideas = Ideas.objects.order_by('-created')
                    return render(request, "network/index.html", {
                        'ideas': ideas,
                    })
        except TypeError:
            ideas = Ideas.objects.order_by('-created')
            return render(request, "network/index.html", {
                'ideas': ideas,
            })
    else:
        ideas = Ideas.objects.order_by('-created')
        paginator = Paginator(ideas, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/index.html", {
            'page_obj': page_obj,
            'paginator': paginator,
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def new_idea(request):
    # Post
    if request.method == "POST":
        # Main var
        form = IdeaForm(request.POST)
        if form.is_valid():
            # If valid save
            newIdea = form.save(commit=False)
            newIdea.author = request.user
            newIdea.save()
            return HttpResponseRedirect(reverse("index"))
        # if invalid form returns semi completed form
        else:
            return render(request, "network/new_idea.html", {
                "form": form
            })
    # Get
    else:
        return render(request, "network/new_idea.html", {
            "form": IdeaForm(),
        })


def user(request, user):
    # Get user
    user_data = User.objects.get(username=user)
    # Get user ideas
    ideas = Ideas.objects.filter(author=user_data.id).order_by('-created')
    nr_posts = ideas.count()
    # Get number of comments
    nr_comments = Comments.objects.filter(commenter=user_data.id).count()
    # Get number of followees
    nr_followees = user_data.followees.all().count()
    paginator = Paginator(ideas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/user.html", {
        'nr_posts': nr_posts,
        'nr_comments': nr_comments,
        'user_data': user_data,
        'nr_followees': nr_followees,
        'page_obj': page_obj,
        'paginator': paginator,
    })


def idea(request, id):
    if request.method == "GET":
        idea = Ideas.objects.get(pk=id)
        return JsonResponse(idea.serialize())
    elif request.method == "POST":
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))


def ideas(request):
    # Get all ideas ordered by last created
    ideas = Ideas.objects.order_by('-created')
    return JsonResponse([idea.serialize() for idea in ideas], safe=False)


def get_user(request, id):
    if request.method == "PUT":
        user = request.user
        user_data = User.objects.get(id=id)
        data = json.loads(request.body)

        if data.get("add") is not None:
            user_data.followers.add(user)
            user.followees.add(user_data.id)
            user.save()
            user_data.save()
            user_data = User.objects.get(id=id)
            return JsonResponse(user_data.serialize())

        if data.get("remove") is not None:
            user_data.followers.remove(user)
            user.followees.remove(user_data)
            user.save()
            user_data.save()
            user_data = User.objects.get(id=id)
            return JsonResponse(user_data.serialize())
    else:
        user_data = User.objects.get(id=id)
        return JsonResponse(user_data.serialize())


def following(request):
    if request.method == 'GET':
        user = request.user
        user_data = User.objects.get(username=user)
        followees = user_data.followees.all()
        ideas = Ideas.objects.filter(author__in=followees).order_by('-created')
        paginator = Paginator(ideas, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/following.html", {
            'page_obj': page_obj,
            'paginator': paginator,
        })
    else:
        return HttpResponseRedirect(reverse("index"))


def edit_idea(request):
    if request.method != 'PUT':
        return HttpResponseRedirect(reverse("index"))
    else:
        data = json.loads(request.body)
        idea = Ideas.objects.get(pk=data.get('id'))
        idea.idea = data.get('idea')
        idea.edited = timezone.now()
        idea.save()

        ideas = Ideas.objects.order_by('-created')
        return render(request, "network/index.html", {
            'ideas': ideas,
        })
