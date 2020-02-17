from django.contrib import admin
from .models import portalUser,Team

# Register your models here.
admin.site.register(portalUser)
# admin.site.register(UserLink)
# admin.site.register(Token)
admin.site.register(Team)
