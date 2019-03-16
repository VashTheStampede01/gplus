# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.
class gundamlist(ListView):
    model = gundam
class gundamdetail(DetailView):
    model = gundam
class weaponlist(ListView):
    model = weapon
class weapondetail(DetailView):
    model = weapon
class pilotlist(ListView):
    model = pilot
class pilotdetail(DetailView):
    model = pilot
class utilslist(ListView):
    model = utils
class utilsdetail(DetailView):
    model = utils

