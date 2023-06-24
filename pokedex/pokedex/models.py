from django.db import models

class pokedex_api_to_get(models.Model):
    pokedex_api = models.TextField()

    def __str__(self):
        template = '{0.pokedex_api}'
        return template.format(self)

class pokedex_api_output(models.Model):
    pokedex_api_output = models.TextField()

    def __str__(self):
        template = '{0.pokedex_api_output}'
        return template.format(self)