from django.contrib import admin
from . models import Convenor,Coordinator,HeadCoordinator,Manager
# Register your models here.
admin.site.register(Convenor)
admin.site.register(Coordinator)
admin.site.register(HeadCoordinator)
admin.site.register(Manager)
