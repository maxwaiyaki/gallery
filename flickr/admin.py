from django.contrib import admin

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    
admin.site.register(Location)
admin.site.register(Image,ImageAdmin)