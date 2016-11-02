from django.db import models

# Create your models here.

class kategori(models.Model):
    kategori = models.CharField(max_length=125)
    slug = models.SlugField()
    tarih = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.slug



class makale(models.Model):
    baslik = models.CharField(max_length=120)
    yazi = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    begenilme = models.IntegerField(default=0)
    kategori = models.ForeignKey(kategori)
    def __unicode__(self):
        return self.baslik


class yorum(models.Model):
    makale = models.ForeignKey(makale)
    yapan = models.CharField(max_length=120)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    begenilme = models.IntegerField(default=0)
    ip = models.IPAddressField(auto_created=True)
    def __unicode__(self):
        return unicode(self.tarih)
