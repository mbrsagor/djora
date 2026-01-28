from django.views import generic
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin


from backend.forms.slider_form import SliderModelForm
from backend.models import Slider


@method_decorator(login_required(login_url='/user/signin/'), name='dispatch')
class AddSliderView(SuccessMessageMixin, generic.CreateView):
    model = Slider
    form_class = SliderModelForm
    template_name = 'features/slider/add_slider.html'
    success_url = '/backend/add-slider/'
    success_message = 'Slider created successfully'



@method_decorator(login_required(login_url='/user/signin/'), name='dispatch')
class SliderListView(generic.ListView):
    """
    Slider listview with pagination
    URL: /core/slider-listview/
    Method: GET
    :param
    """
    model = Slider
    paginate_by = 8
    context_object_name = 'sliders'
    filterset_fields = ['title', 'subtitle']
    template_name = 'features/slider/slider_listview.html'


@method_decorator(login_required(login_url='/user/signin/'), name='dispatch')
class SliderUpdateView(SuccessMessageMixin, generic.UpdateView):
    """
    Slider update view
    URL: /core/slider-update/<pk>/
    Method: PUT
    :param
    """
    model = Slider
    form_class = SliderModelForm
    success_message = 'Slider has been updated'
    template_name = 'features/slider/add_slider.html'

    def get_success_url(self):
        return reverse('slider_update', kwargs={'pk': self.object.id})


@method_decorator(login_required(login_url='/user/signin/'), name='dispatch')
class SliderDeleteView(SuccessMessageMixin, generic.DeleteView):
    """
    Slider Delete View
    URL: /backend/slider-delete/<pk>/
    Method: DELETE
    """
    model = Slider
    success_url = '/backend/slider-listview/'
    success_message = 'Slider has been deleted.'
    template_name = 'common/delete_confirm.html'
