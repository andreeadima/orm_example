from django.views.generic import ListView
from orm_example import models
# Create your views here.


class HomeView(ListView):
    template_name = 'home.html'
    model = models.Post
    context_object_name = 'list'

    def get_queryset(self):
        return models.Post.objects.all()
        # return models.Post.objects.filter(user__first_name__contains='Alex')
        # return models.Post.objects.exclude(user__first_name='Andreea')
        # return models.Post.objects.get(pk=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['sql'] = self.get_queryset().query
        except:
            pass
        return context
