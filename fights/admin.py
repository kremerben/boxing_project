from django.contrib import admin

# Register your models here.
from fights.models import Organization, Manager, Fighter, Bout, Belt, Promoter


class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name','acronym')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('location', 'est_date')
        }),
    )
    list_display = ('name','acronym', 'location', 'est_date')
    list_filter = ('location', 'est_date')

admin.site.register(Organization, OrganizationAdmin)

class BeltAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight_class', 'boxing_organization')
    list_filter = ('boxing_organization',)

admin.site.register(Belt, BeltAdmin)

class FighterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name', 'wins', 'losses', 'weight_class')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('weight', 'height', 'reach', 'manager')
        }),
    )
    list_display = ('name', 'wins', 'losses', 'weight_class', 'weight', 'height', 'reach', 'manager')
    list_filter = ('wins', 'losses', 'weight_class', 'weight', 'height', 'reach', 'manager', 'manager')

admin.site.register(Fighter, FighterAdmin)
admin.site.register(Manager)

class BoutAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('winner', 'fighter1', 'fighter2', 'date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('fighter1_score', 'fighter2_score')
        }),
    )
    list_display = ('winner', 'fighter1', 'fighter2', 'date')
    list_filter = ('winner', 'fighter1', 'fighter2', 'date')


admin.site.register(Bout, BoutAdmin)
admin.site.register(Promoter)
