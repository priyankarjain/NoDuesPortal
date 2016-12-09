from django.contrib import admin
from . import models

admin.site.register(models.Choice)
admin.site.register(models.User)
admin.site.register(models.Prof)
admin.site.register(models.Caretaker)
admin.site.register(models.Warden)
admin.site.register(models.HeadOfDep)
admin.site.register(models.Student)
admin.site.register(models.Administrative)
admin.site.register(models.Nodue,models.NoDueAdmin)
admin.site.register(models.GrantClearance,models.ClearanceAdmin)