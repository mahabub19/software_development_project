from django.contrib import admin
from .models import feedbacks

# Register your models here.

class FeedbacksAdmin(admin.ModelAdmin):
    list_display=('name','image','message','created')

admin.site.register(feedbacks,FeedbacksAdmin)
