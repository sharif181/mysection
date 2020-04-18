from django.contrib import admin
from .models import quiz,presentation,assignment,Announcement

admin.site.register(quiz)
admin.site.register(presentation)
admin.site.register(assignment)
admin.site.register(Announcement)