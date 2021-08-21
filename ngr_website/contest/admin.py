from django.contrib import admin
from .models import Contest, Contestant, Vote

# Register your models here.

admin.site.register(Contest)
admin.site.register(Contestant)
admin.site.register(Vote)
