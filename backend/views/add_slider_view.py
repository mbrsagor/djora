from django.views import generic
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin


from backend.forms.slider_form import SliderModelForm
from backend.models import Slider


@method_decorator(login_required(login_url='/core/signin/'), name='dispatch')
class AddSliderView(SuccessMessageMixin, generic.CreateView):
    model = Slider
    form_class = SliderModelForm
    template_name = 'features/slider/add_slider.html'
    success_url = '/backend/add-slider/'
    success_message = 'Slider created successfully'
