from django.contrib import admin
from testAPI.models import *


admin.site.site_header  =  "egera Policy" 
admin.site.site_title  =  "egera Policy admin site"
admin.site.index_title  =  "egera Policy Admin"



class AdminSong(admin.ModelAdmin):
    list_display = ['numero', 'rrr', 'title_1', 'title_2', 'indirimbo', 'categorie']
    list_editable = ['rrr', 'title_1', 'title_2', 'indirimbo', 'categorie']
    #list_per_page = 10
    # actions = [export_as_csv_action()]

admin.site.register(Song, AdminSong)