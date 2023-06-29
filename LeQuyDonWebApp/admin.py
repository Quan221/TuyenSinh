from django.contrib import admin
from .models import Quan, Phuong, User, DonTuyenSinh, QuanvaPhuong , DaHocHetLop5, TruongVaQuan, Truong, DangKyHoc
from .actions import export_as_csv, export_to_excel
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DonTuyenSinh._meta.fields]
    actions = [export_to_excel]

admin.site.register(Quan)
admin.site.register(Phuong)
admin.site.register(User)
admin.site.register(DonTuyenSinh,MyModelAdmin)
admin.site.register(QuanvaPhuong)
admin.site.register(DaHocHetLop5)
admin.site.register(Truong)
admin.site.register(TruongVaQuan)
admin.site.register(DangKyHoc)


