from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class Paket_tour(models.Model):
    nama_paket = models.CharField(max_length=200)
    poto       = models.ImageField(upload_to='paket_tour', default='')  
    durasi     = models.CharField(max_length=200)
    harga      = models.CharField(max_length=200)
    detail_harga = models.ManyToManyField('Detail_harga')
    list_paket = models.ManyToManyField('List_tour', related_name='list_pakets')
    def __str__(self):
        return self.nama_paket


class List(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class Detail_harga(models.Model):
    harga = models.CharField(max_length=200)
    jumlah = models.CharField(max_length=200)

    def __str__(self):
        return self.harga


class List_tour(models.Model):
    hari  = models.CharField(max_length=200)
    list  = models.ManyToManyField('List', related_name='lists')

    def __str__(self):
        return self.hari

class Paket_transport(models.Model):
    nama_tujuan = models.CharField(max_length=200) 
    harga       = models.IntegerField()


    def __str__(self):
        return self.nama_tujuan




class Pesanan_paket(models.Model):
    nama          = models.CharField(max_length=200)
    alamat        = models.CharField(max_length=200)
    nomor_hp      = models.CharField(max_length=200)
    jumlah_orang  = models.CharField(max_length=100)
    tanggal_jemput= models.DateField()
    paket         = models.CharField(max_length=200)


    def __str__(self):
        return self.nama


class Galeri(models.Model):
    judul = models.CharField(max_length=200)
    poto = models.ImageField(upload_to='galeri', default='')

    def __str__(self):
        return self.judul


class Kontak(models.Model):
    nama  = models.CharField(max_length=100) 
    email = models.EmailField()
    pesan = models.TextField()


    def __str__(self):
        return self.nama



        