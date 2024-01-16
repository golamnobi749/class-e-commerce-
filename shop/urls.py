from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home ,name='home'),
    path('tshirt/',views.TshirtView.as_view() ,name='tshirt'),
    path('tshirtview/<int:pk>',views.ProductViews.as_view(),name='tshirtview'),


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)