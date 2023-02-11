from django.urls import path
from django.views import generic
from . import views

class IndexView(generic.TemplateView):
    template_name = 'index.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
]