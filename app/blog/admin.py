from django.contrib import admin
from blog.models import makale, yorum, kategori
# Register your models here.
class makaleAdmin(admin.ModelAdmin):
    search_fields = ["baslik"]
    list_display = [  "baslik","id", "tarih", "begenilme"]
    list_display_links = [  "baslik","id", "tarih", "begenilme"]
    prepopulated_fields = {"slug" : ("baslik",)}

class yorumAdmin(admin.ModelAdmin):
    list_display = ["yapan", "tarih", "makale", "begenilme"]
    list_display_links = ["yapan", "tarih", "makale", "begenilme"]

class kategoriAdmin(admin.ModelAdmin):
    list_display = ["kategori", "slug"]
    list_display_links = ["kategori", "slug"]
    prepopulated_fields = {"slug" : ("kategori",)}


admin.site.register(makale, makaleAdmin)
admin.site.register(yorum, yorumAdmin)
admin.site.register(kategori, kategoriAdmin)