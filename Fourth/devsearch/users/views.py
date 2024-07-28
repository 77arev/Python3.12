from django.shortcuts import render, redirect


# from .models import Profile
# from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib import messages
# from .forms import CustomUserCreationForm, ProfileForm, SkillForm
# from django.contrib.auth.decorators import login_required
# from .utils import search_profiles

# Create your views here.

# def profiles(request):
#     prof, search_query = search_profiles(request)
#     context = {"profiles": prof, "search_query": search_query}
#     return render(request, 'users/index.html', context)

def profiles(request):
    return render(request, 'users/index.html')


