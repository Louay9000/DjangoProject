from django.contrib import admin
from .models import Venue, MonClubUser
from .models import Evenement
from .models import MonClubUser

#admin.site.register(Venue)
admin.site.register(MonClubUser)
#admin.site.register(Evenement)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')
    
    
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    fields = (('name','venue'), 'evenement_date', 'description', 'manager','attendees', 'approved')
    list_display = ('name','evenement_date', 'venue')
    list_filter = ('evenement_date', 'venue')
    ordering = ('-evenement_date',)
        
        
