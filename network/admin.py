from django.contrib import admin
from .models import User, Comments, Ideas


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


class IdeasAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Ideas, IdeasAdmin)
