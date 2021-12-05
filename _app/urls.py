from django.urls import path

from .import views

app_name = '_app'

urlpatterns = [
    path('', views.home, name='index'),
    path('paket-tour/detail/<int:id>', views.detail, name='detail'),
    path('kontak/', views.kontak, name='kontak'),
    path('paket/', views.paket, name='paket'),
    path('transport/', views.transport, name='transport'),
    path('tentang-kami/', views.tentang_kami, name='tentang_kami'),
    path('galeri/', views.galeri, name='galeri'),

]