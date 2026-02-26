from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect(reverse('storage:list'))

        return super().dispatch(request, *args, **kwargs)
