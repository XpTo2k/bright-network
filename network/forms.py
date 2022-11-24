from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import Ideas

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ("title", "idea",)
        labels = {
            "title" : "",
            "idea" : "",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder" : "write a short title, limit 32 bytes.",
                }),
            "idea": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder" : "express your idea, limit 2048 bytes."
                }),
        }