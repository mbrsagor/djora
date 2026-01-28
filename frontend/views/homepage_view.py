from django.views import generic



# Homepage View
class HomePageView(generic.TemplateView):
    template_name = 'home/homepage.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
 