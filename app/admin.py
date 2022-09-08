from django.contrib import admin

from app.models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    readonly_fields = ("pokeapi_id", "name", "height", "order", "weight")


admin.site.register(Pokemon, PokemonAdmin)
