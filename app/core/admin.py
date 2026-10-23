from django.contrib import admin

# Register your models here.
from .models import KhachHang, TuongTac

admin.site.register(KhachHang)
admin.site.register(TuongTac)
