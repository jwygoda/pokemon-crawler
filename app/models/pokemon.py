from django.db import models


class Pokemon(models.Model):
    pokeapi_id = models.PositiveSmallIntegerField()
    name = models.TextField()
    description = models.TextField()
    height = models.PositiveSmallIntegerField()
    order = models.SmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    # fields such as abilities, moves and stats would be m2ms with a through model

    def __str__(self):
        return self.name
