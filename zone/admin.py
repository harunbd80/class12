from django.contrib import admin
from zone.models import info
# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display=('id','frist_name','last_name','email','serial','password','repassword','text','chackbox','payment','django')

admin.site.register(info,infoAdmin)