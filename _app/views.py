from django.db.models.fields import EmailField
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import ( 
    Paket_transport, Paket_tour, Pesanan_paket, Kontak, List, List_tour, Pesanan_paket )

def home(request):
    paket_tour = Paket_tour.objects.all()
    context = {
        'judul':'Home',
        'paket_tours': paket_tour
    }

    return render(request,"home.html", context)


def detail(request, id):
    paket = Paket_tour.objects.get(id=id)
    paket_list_hari  = paket.list_paket.all()

    print(paket. __dict__)
    
    context = {
        'title':'Detail',
        'paket': paket,
        'paket_list_hari': paket_list_hari
    }

    if request.method == 'POST':
        Pesanan_paket.objects.create(
            nama            = request.POST.get('nama'),
            alamat          = request.POST.get('alamat'),
            nomor_hp        = request.POST.get('nomor_hp'),
            jumlah_orang    = request.POST.get('jumlah_orang'),
            tanggal_jemput  = request.POST.get('tanggal_penjemputan'),
            paket           = paket.nama_paket
        )

        Pesanan_paket.save
        messages.success(request,'Pemesanan paket sukses, kami akan menghubungi anda via telepon')

        return redirect('_app:index')
    return render(request,'detail.html',context)

def kontak(request):
    context = {
        'title':'Kontak'
    }

    if request.method == 'POST':
        nama  = request.POST.get('nama')
        email = request.POST.get('email')
        pesan = request.POST.get('pesan')

        Kontak.objects.create(
            nama = nama,
            email =email,
            pesan = pesan
        )
        Kontak.save
        messages.success(request,'Terimakasih, pesan anda sudah terkirim')

    else:
        return render(request,'kontak.html',context)    

    return render(request,'kontak.html',context)


def paket(request):
    return render(request,'paket.html')

def transport(request):
    paket_transports = Paket_transport.objects.all()
    context = {
        'paket_transport': paket_transports
    }

    return render(request,'transport.html', context)


def tentang_kami(request):

    return render(request,'tentang_kami.html',context={})
    

def galeri(request):

    return render(request,'galeri.html',context={})


def error_404(request, exception):
    return render(request,'404.html')





