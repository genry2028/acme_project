from django.contrib import admin
from .models import Birthday, Congratulation, Tag


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    pass


@admin.register(Congratulation)
class CongratulationAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
