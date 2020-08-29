from django.contrib import admin
from . models import Bus, Booking

class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_no', 'from_city','to_city','no_of_seats','price','date', 'time')
    list_display_links = ('bus_no',)
    list_filter = ('bus_no',)
    search_fields = ('bus_no','date')
    list_per_page = 30
admin.site.register(Bus, BusAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','bus', 'first_name','last_name', 'from_city','to_city','phone', 'email', 'price','date', 'time')
    list_display_links = ('user','bus')
    list_filter = ('email','phone')
    search_fields = ('email','phone')
    list_per_page = 30
admin.site.register(Booking, BookingAdmin)


