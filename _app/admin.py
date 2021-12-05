from django.contrib import admin
from .models import Kontak, Paket_tour, Paket_transport, Pesanan_paket,List_tour, List, Detail_harga
# Register your models here.


admin.site.register(Paket_tour)
admin.site.register(Paket_transport)
admin.site.register(Pesanan_paket)
admin.site.register(Kontak)
admin.site.register(List)
admin.site.register(List_tour)
admin.site.register(Detail_harga)