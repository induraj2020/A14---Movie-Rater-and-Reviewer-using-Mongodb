from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Movies
from import_export.admin import ImportExportModelAdmin
from import_export import resources


admin.site.site_header ='Admin Dashboard '
admin.site.site_title = 'Welcome Admin'

#class MovieAdmin(admin.ModelAdmin):
 #   list_display = ('title','font_size')
  #  list_filter = ('year',)
    #change_list_template = 'homescreen/homescreen/templates/base.html'

#admin.site.register(Movies)

class MovieResource(resources.ModelResource):
    class Meta:
        model = Movies


@admin.register(Movies)
class MoviesAdmin(ImportExportModelAdmin, ):
    pass
