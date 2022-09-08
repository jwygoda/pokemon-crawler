import asyncio

import aiopoke
from django.core.management.base import BaseCommand

from app.models import Pokemon


async def update_or_create_pokemon(client, pokemon_id):
    response = await client.get_pokemon(pokemon_id)
    return await Pokemon.objects.aupdate_or_create(
        pokeapi_id=response.id,
        defaults={
            "name": response.name,
            "height": response.height,
            "order": response.order,
            "weight": response.weight,
        },
    )


async def main():
    # TODO: handle api failures
    client = aiopoke.AiopokeClient()
    pokemons = await client.http.get("pokemon/?limit=-1")
    ids = [pokemon["url"].split("/")[-2] for pokemon in pokemons["results"]]
    tasks = [update_or_create_pokemon(client, pokemon_id) for pokemon_id in ids]
    return await asyncio.gather(*tasks)


class Command(BaseCommand):
    help = "Updates pokemons from PokeAPI"

    def handle(self, *args, **options):
        asyncio.run(main())
