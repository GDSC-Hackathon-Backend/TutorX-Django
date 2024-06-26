from django.contrib import admin
from .models import *
from user.models import CustomUser,Tutor,Client

@admin.register(TutorBooking)
class TutorBookingAdmin(admin.ModelAdmin):
    list_display = ['client_full_name', 'tutor_full_name', 'is_virtual', 'is_in_person', 'created_at']
    def client_full_name(self, obj):
        return obj.client.user.full_name  if obj.client else ''

    def tutor_full_name(self, obj):
        return obj.tutor.user.full_name if obj.tutor else ''

@admin.register(TutorNotification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'message', 'created_at','is_approved','is_declined')

    def client_username(self, obj):
        return obj.client.user.username
    
    client_username.short_description = 'Client Username'
@admin.register(ClientNotification)
class NotificationCAdmin(admin.ModelAdmin):
    list_display = ('tutor_username', 'message', 'created_at')

    def tutor_username(self, obj):
        return obj.tutor.user.username
    
    tutor_username.short_description = 'Tutor Username'
@admin.register(OngoingJob)
class ongoingjobAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'start_date')

    def client_username(self, obj):
        return obj.client.user.username
    
    client_username.short_description = 'Client Username'
@admin.register(CompletedJob)
class completedjobAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'end_date')

    def client_username(self, obj):
        return obj.client.user.username
    
    client_username.short_description = 'Client Username'

@admin.register(TutorRequest)
class TutorRequestAdmin(admin.ModelAdmin):
    list_display = ('client_username','message', 'created_at')
    def client_username(self, obj):
        return obj.client.user.username
    
    client_username.short_description = 'Client Username'
@admin.register(TutorRating)
class TutorRatingAdmin(admin.ModelAdmin):
    list_display = ('client_full_name','rating', 'comment','tutor_full_name')
    def client_full_name(self, obj):
        return obj.client.user.full_name
    def tutor_full_name(self, obj):
        return obj.tutor.user.full_name
    
    #tutor_full_name.short_description = 'Tutor Username'
    

