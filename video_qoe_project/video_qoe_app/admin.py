from django.contrib import admin
from .models import QoeRating, QoeVideo, ValidationVideo
#from django.contrib.auth.models import Group

# Custom setup of admin page
admin.site.site_header = "Video QoE Survey"

# class QoeVideoAdmin(admin.ModelAdmin):
#     list_display = ( 'video_id', 'video_name', 'packet_loss_value', 'rtt_value', 'network', 'video_file_path', ) # this is a tuple
#     list_filter = ['video_id'] # this is a list




# Register your models here.
admin.site.register(QoeRating)
admin.site.register(ValidationVideo)
admin.site.register(QoeVideo)
#admin.site.register(QoeVideo, QoeVideoAdmin)

