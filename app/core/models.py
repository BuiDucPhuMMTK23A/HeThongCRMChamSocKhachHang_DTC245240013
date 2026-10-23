from django.db import models

class KhachHang(models.Model):
    ten = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.ten

class TuongTac(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    noi_dung = models.TextField()
    ngay = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.khach_hang.ten} - {self.ngay.strftime('%d/%m/%Y')}"
