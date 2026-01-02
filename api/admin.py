from django.contrib import admin
from .models import Talaba, Tolov, IshHaqqi, Qarzdor, QarzMiqdori



@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'telefon', 'balans')
    search_fields = ('full_name', 'telefon')
    list_filter = ('balans',)


@admin.register(Tolov)
class TolovAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'talaba',
        'summa',
        'turi',
        'xodim',
        'sana'
    )
    list_filter = ('turi', 'sana')
    search_fields = ('talaba__full_name', 'xodim')


@admin.register(IshHaqqi)
class IshHaqqiAdmin(admin.ModelAdmin):
    list_display = ('maosh_turi', 'miqdori', 'oqituvchi', 'guruh')
    list_filter = ('maosh_turi', 'guruh')


@admin.register(Qarzdor)
class QarzdorAdmin(admin.ModelAdmin):
    list_display = ('ism', 'telefon', 'jami_qarz', 'holati')
    list_filter = ('holati',)


@admin.register(QarzMiqdori)
class QarzMiqdoriAdmin(admin.ModelAdmin):
    list_display = ('qarzdor', 'miqdor', 'sana')
