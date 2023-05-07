from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "phonenumber","age", "blood_group", "address", "volume_of_blood_donated")
  
admin.site.register(Member, MemberAdmin)

