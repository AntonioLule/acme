from django.shortcuts import render
from django.http import HttpResponseRedirect
# Generic views
from django.views.generic import CreateView
from django.views import View
# ----- Django ---- #
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token

from django.contrib import messages
from django.db.models import Q

# Forms
from purchases_sales.forms import *
# Models
from purchases_sales.models import *
#Enums
from utils.enums import Category, TypeOperation


class RegisterView(CreateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    form_class = StoreUserCreationForm
    template_name = 'registration/register.html'


    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['form'] =  self.form_class(self.request.GET)

        return context

    def post(self, request, *data, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            try: 
                form.save()
                messages.success(request, "Registrado Correctamente")
                return HttpResponseRedirect(self.login_url)
            except Exception as er:
                messages.error(request, er.args)
                return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class HomeView(LoginRequiredMixin, View):
    
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'purchases_sales/create.html'


    def get(self, request, *data, **kwargs):
        user = request.user  # Obtener el usuario logueado
        token, created = Token.objects.get_or_create(user=user) #token para las apis

        context = dict()
        context['category'] = [(category.value, category.name) for category in Category]
        context['type_operation'] = [(type_op.value, type_op.name) for type_op in TypeOperation]
        context['user_id'] = user.id
        context['token'] = token
        

        return render(request, self.template_name, context)