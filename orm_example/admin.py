from django.contrib import admin
from orm_example import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Comment)
admin.site.register(models.Post)

