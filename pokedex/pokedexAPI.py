# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2023
# Copyright (c) 2023 John Capobianco

# ----------------
# Python
# ----------------
import json
import urllib3
import requests
import rich_click as click
import django
django.setup()
from pokedex.models import pokedex_api_to_get,pokedex_api_output

urllib3.disable_warnings()

db_api = pokedex_api_to_get.objects.all().values('pokedex_api')

api = db_api[0]['pokedex_api']

class pokedex_Plugin():
    def pokedex_plugin(self):
        self.get_json()
   
    def get_json(self):
        payload={}
        headers = {}
        response = requests.request("GET", api, headers=headers, data=payload)
        all_json = response.json()
        if api == "https://pokeapi.co/api/v2/pokemon?limit=1500":
            pokemon_names = []
            for pokemon in all_json['results']:
                pokemon_name = pokemon['name']
                pokemon_names.append(pokemon_name)
        if "/pokemon/" in api:
            for ability in all_json['abilities']:
                del(ability['ability']['url'])
                del(ability['slot'])
            for form in all_json['forms']:
                del(form['url'])
            del(all_json['game_indices'])
            del(all_json['id'])
            del(all_json['is_default'])
            del(all_json['location_area_encounters'])
            for move in all_json['moves']:
                del(move['move']['url'])
                del(move['version_group_details'])
            del(all_json['order'])
            del(all_json['past_types'])
            del(all_json['species']['url'])
            del(all_json['sprites']['other'])
            del(all_json['sprites']['versions'])
            for stat in all_json['stats']:
                del(stat['stat']['url'])
            for type in all_json['types']:
                del(type['slot'])
                del(type['type']['url'])            

        if api == "https://pokeapi.co/api/v2/pokemon?limit=1500":
            chatGPTAnswer=pokedex_api_output(pokedex_api_output = json.dumps(pokemon_names,sort_keys=True,indent=4))
            chatGPTAnswer.save()    
        else:
            chatGPTAnswer=pokedex_api_output(pokedex_api_output = json.dumps(all_json,sort_keys=True,indent=4))
            chatGPTAnswer.save()    

        deleteme = pokedex_api_to_get.objects.all()
        deleteme.delete()

@click.command()
def cli():
    invoke_class = pokedex_Plugin()
    invoke_class.pokedex_plugin()

if __name__ == "__main__":
    cli()