from django.contrib import admin
from .models import Topic
from django.contrib.auth.models import User

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poster Information', {'fields': ['user_who_posted']}),
        ('Topic Information', {'fields': ['topic_text', 'description_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

    # Cannot change who posted the topic
    # For now I'll be able to cahnge topix info and description info
    # for testing and stuff
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user_who_posted','pub_date',)
        return self.readonly_fields

# Classes must be above the registration
admin.site.register(Topic, TopicAdmin)
