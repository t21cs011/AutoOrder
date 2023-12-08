from django.views.generic import ListView
from .models import User,Item
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy
# Create your views here.
class UserHomeView(TemplateView):
    model = User
    template_name = 'user_home.html'
    
class BuyItemView(TemplateView):
    model = Item
    template_name = 'userhome/buy_item.html'
    
class BuyHistoryView(TemplateView):
    model = Item
    template_name = 'userhome/buy_history.html'
    
class ChangePassView(TemplateView):
    model = User
    template_name = 'userhome/change_pass.html'
    
    