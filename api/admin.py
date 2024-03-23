from django.contrib import admin
from .models import Topic, Record, User

# Register your models here.
admin.site.register(Topic)
admin.site.register(Record)
admin.site.register(User)
