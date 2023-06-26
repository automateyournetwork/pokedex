import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import pokedex_api_to_get,pokedex_api_output

def pokemon_all_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api = "https://pokeapi.co/api/v2/pokemon?limit=1500")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bulbasaur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ivysaur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/2/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_venusaur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/3/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_charmander_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/4/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_charmeleon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/5/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_charizard_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/6/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_squirtle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/7/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wartortle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/8/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_blastoise_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/9/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_caterpie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_metapod_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/11/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_butterfree_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/12/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_weedle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/13/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kakuna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/14/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_beedrill_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/15/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pidgey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/16/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pidgeotto_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/17/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pidgeot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/18/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rattata_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/19/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_raticate_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/20/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spearow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/21/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fearow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/22/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ekans_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/23/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arbok_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/24/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pikachu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/25/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_raichu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/26/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sandshrew_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/27/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sandslash_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/28/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nidoran_f_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/29/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nidorina_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/30/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nidoqueen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/31/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nidoran_m_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/32/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nidorino_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/33/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nidoking_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/34/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clefairy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/35/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clefable_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/36/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vulpix_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/37/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ninetales_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/38/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jigglypuff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/39/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wigglytuff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/40/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zubat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/41/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_golbat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/42/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_oddish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/43/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gloom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/44/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vileplume_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/45/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_paras_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/46/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_parasect_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/47/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_venonat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/48/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_venomoth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/49/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_diglett_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/50/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dugtrio_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/51/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meowth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/52/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_persian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/53/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_psyduck_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/54/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_golduck_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/55/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mankey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/56/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_primeape_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/57/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_growlithe_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/58/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arcanine_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/59/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_poliwag_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/60/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_poliwhirl_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/61/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_poliwrath_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/62/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_abra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/63/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kadabra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/64/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_alakazam_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/65/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_machop_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/66/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_machoke_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/67/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_machamp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/68/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bellsprout_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/69/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_weepinbell_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/70/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_victreebel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/71/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tentacool_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/72/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tentacruel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/73/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_geodude_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/74/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_graveler_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/75/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_golem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/76/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ponyta_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/77/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rapidash_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/78/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slowpoke_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/79/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slowbro_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/80/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magnemite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/81/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magneton_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/82/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_farfetchd_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/83/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_doduo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/84/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dodrio_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/85/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_seel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/86/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dewgong_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/87/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grimer_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/88/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_muk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/89/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shellder_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/90/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cloyster_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/91/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gastly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/92/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_haunter_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/93/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gengar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/94/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_onix_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/95/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drowzee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/96/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hypno_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/97/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_krabby_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/98/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kingler_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/99/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_voltorb_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/100/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_electrode_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/101/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_exeggcute_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/102/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_exeggutor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/103/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cubone_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/104/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_marowak_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/105/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hitmonlee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/106/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hitmonchan_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/107/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lickitung_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/108/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_koffing_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/109/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_weezing_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/110/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rhyhorn_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/111/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rhydon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/112/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chansey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/113/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tangela_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/114/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kangaskhan_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/115/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_horsea_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/116/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_seadra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/117/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_goldeen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/118/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_seaking_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/119/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_staryu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/120/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_starmie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/121/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mr_mime_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/122/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scyther_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/123/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jynx_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/124/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_electabuzz_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/125/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magmar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/126/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pinsir_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/127/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tauros_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/128/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magikarp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/129/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gyarados_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/130/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lapras_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/131/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ditto_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/132/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_eevee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/133/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vaporeon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/134/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jolteon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/135/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flareon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/136/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_porygon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/137/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_omanyte_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/138/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_omastar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/139/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kabuto_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/140/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kabutops_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/141/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aerodactyl_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/142/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_snorlax_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/143/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_articuno_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/144/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zapdos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/145/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_moltres_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/146/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dratini_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/147/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dragonair_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/148/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dragonite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/149/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mewtwo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/150/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mew_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/151/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chikorita_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/152/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bayleef_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/153/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meganium_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/154/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cyndaquil_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/155/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_quilava_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/156/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_typhlosion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/157/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_totodile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/158/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_croconaw_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/159/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_feraligatr_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/160/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sentret_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/161/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_furret_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/162/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hoothoot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/163/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_noctowl_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/164/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ledyba_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/165/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ledian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/166/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spinarak_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/167/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ariados_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/168/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_crobat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/169/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chinchou_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/170/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lanturn_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/171/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pichu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/172/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cleffa_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/173/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_igglybuff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/174/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_togepi_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/175/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_togetic_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/176/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_natu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/177/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_xatu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/178/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mareep_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/179/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flaaffy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/180/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ampharos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/181/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bellossom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/182/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_marill_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/183/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_azumarill_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/184/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sudowoodo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/185/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_politoed_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/186/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hoppip_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/187/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skiploom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/188/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jumpluff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/189/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aipom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/190/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sunkern_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/191/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sunflora_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/192/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_yanma_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/193/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wooper_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/194/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_quagsire_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/195/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_espeon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/196/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_umbreon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/197/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_murkrow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/198/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slowking_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/199/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_misdreavus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/200/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_unown_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/201/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wobbuffet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/202/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_girafarig_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/203/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pineco_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/204/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_forretress_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/205/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dunsparce_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/206/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gligar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/207/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_steelix_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/208/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_snubbull_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/209/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_granbull_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/210/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_qwilfish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/211/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scizor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/212/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shuckle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/213/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_heracross_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/214/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sneasel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/215/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_teddiursa_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/216/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ursaring_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/217/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slugma_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/218/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magcargo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/219/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swinub_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/220/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_piloswine_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/221/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_corsola_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/222/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_remoraid_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/223/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_octillery_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/224/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_delibird_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/225/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mantine_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/226/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skarmory_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/227/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_houndour_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/228/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_houndoom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/229/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kingdra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/230/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_phanpy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/231/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_donphan_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/232/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_porygon2_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/233/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stantler_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/234/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_smeargle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/235/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tyrogue_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/236/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hitmontop_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/237/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_smoochum_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/238/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_elekid_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/239/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magby_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/240/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_miltank_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/241/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_blissey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/242/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_raikou_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/243/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_entei_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/244/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_suicune_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/245/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_larvitar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/246/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pupitar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/247/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tyranitar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/248/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lugia_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/249/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ho_oh_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/250/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_celebi_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/251/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_treecko_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/252/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grovyle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/253/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sceptile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/254/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_torchic_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/255/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_combusken_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/256/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_blaziken_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/257/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mudkip_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/258/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_marshtomp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/259/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swampert_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/260/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_poochyena_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/261/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mightyena_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/262/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zigzagoon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/263/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_linoone_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/264/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wurmple_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/265/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_silcoon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/266/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_beautifly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/267/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cascoon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/268/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dustox_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/269/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lotad_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/270/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lombre_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/271/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ludicolo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/272/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_seedot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/273/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nuzleaf_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/274/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shiftry_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/275/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_taillow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/276/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swellow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/277/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wingull_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/278/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pelipper_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/279/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ralts_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/280/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kirlia_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/281/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gardevoir_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/282/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_surskit_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/283/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_masquerain_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/284/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shroomish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/285/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_breloom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/286/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slakoth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/287/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vigoroth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/288/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slaking_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/289/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nincada_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/290/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ninjask_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/291/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shedinja_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/292/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_whismur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/293/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_loudred_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/294/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_exploud_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/295/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_makuhita_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/296/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hariyama_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/297/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_azurill_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/298/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nosepass_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/299/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skitty_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/300/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_delcatty_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/301/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sableye_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/302/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mawile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/303/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aron_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/304/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lairon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/305/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aggron_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/306/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meditite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/307/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_medicham_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/308/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_electrike_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/309/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_manectric_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/310/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_plusle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/311/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_minun_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/312/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_volbeat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/313/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_illumise_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/314/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_roselia_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/315/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gulpin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/316/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swalot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/317/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_carvanha_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/318/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sharpedo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/319/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wailmer_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/320/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wailord_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/321/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_numel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/322/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_camerupt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/323/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_torkoal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/324/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spoink_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/325/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grumpig_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/326/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spinda_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/327/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_trapinch_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/328/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vibrava_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/329/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flygon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/330/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cacnea_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/331/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cacturne_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/332/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swablu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/333/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_altaria_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/334/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zangoose_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/335/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_seviper_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/336/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lunatone_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/337/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_solrock_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/338/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_barboach_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/339/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_whiscash_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/340/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_corphish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/341/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_crawdaunt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/342/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_baltoy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/343/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_claydol_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/344/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lileep_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/345/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cradily_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/346/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_anorith_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/347/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_armaldo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/348/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_feebas_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/349/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_milotic_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/350/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_castform_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/351/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kecleon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/352/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shuppet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/353/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_banette_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/354/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_duskull_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/355/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dusclops_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/356/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tropius_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/357/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chimecho_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/358/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_absol_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/359/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wynaut_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/360/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_snorunt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/361/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_glalie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/362/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spheal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/363/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sealeo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/364/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_walrein_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/365/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clamperl_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/366/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_huntail_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/367/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gorebyss_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/368/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_relicanth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/369/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_luvdisc_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/370/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bagon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/371/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shelgon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/372/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_salamence_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/373/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_beldum_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/374/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_metang_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/375/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_metagross_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/376/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_regirock_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/377/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_regice_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/378/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_registeel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/379/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_latias_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/380/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_latios_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/381/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kyogre_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/382/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_groudon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/383/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rayquaza_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/384/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jirachi_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/385/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_deoxys_normal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/386/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_turtwig_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/387/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grotle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/388/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_torterra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/389/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chimchar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/390/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_monferno_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/391/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_infernape_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/392/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_piplup_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/393/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_prinplup_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/394/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_empoleon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/395/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_starly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/396/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_staravia_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/397/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_staraptor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/398/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bidoof_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/399/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bibarel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/400/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kricketot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/401/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kricketune_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/402/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shinx_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/403/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_luxio_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/404/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_luxray_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/405/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_budew_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/406/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_roserade_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/407/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cranidos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/408/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rampardos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/409/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shieldon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/410/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bastiodon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/411/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_burmy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/412/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wormadam_plant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/413/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mothim_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/414/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_combee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/415/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vespiquen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/416/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pachirisu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/417/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_buizel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/418/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_floatzel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/419/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cherubi_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/420/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cherrim_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/421/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shellos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/422/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gastrodon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/423/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ambipom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/424/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drifloon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/425/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drifblim_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/426/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_buneary_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/427/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lopunny_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/428/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mismagius_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/429/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_honchkrow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/430/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_glameow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/431/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_purugly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/432/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chingling_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/433/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stunky_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/434/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skuntank_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/435/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bronzor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/436/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bronzong_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/437/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bonsly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/438/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mime_jr_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/439/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_happiny_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/440/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chatot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/441/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spiritomb_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/442/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gible_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/443/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gabite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/444/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_garchomp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/445/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_munchlax_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/446/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_riolu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/447/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lucario_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/448/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hippopotas_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/449/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hippowdon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/450/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skorupi_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/451/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drapion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/452/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_croagunk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/453/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toxicroak_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/454/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_carnivine_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/455/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_finneon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/456/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lumineon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/457/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mantyke_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/458/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_snover_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/459/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_abomasnow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/460/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_weavile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/461/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magnezone_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/462/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lickilicky_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/463/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rhyperior_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/464/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tangrowth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/465/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_electivire_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/466/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magmortar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/467/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_togekiss_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/468/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_yanmega_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/469/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_leafeon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/470/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_glaceon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/471/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gliscor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/472/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mamoswine_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/473/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_porygon_z_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/474/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gallade_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/475/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_probopass_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/476/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dusknoir_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/477/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_froslass_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/478/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rotom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/479/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_uxie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/480/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mesprit_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/481/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_azelf_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/482/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dialga_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/483/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_palkia_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/484/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_heatran_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/485/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_regigigas_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/486/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_giratina_altered_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/487/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cresselia_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/488/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_phione_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/489/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_manaphy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/490/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_darkrai_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/491/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shaymin_land_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/492/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arceus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/493/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_victini_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/494/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_snivy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/495/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_servine_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/496/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_serperior_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/497/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tepig_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/498/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pignite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/499/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_emboar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/500/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_oshawott_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/501/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dewott_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/502/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_samurott_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/503/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_patrat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/504/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_watchog_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/505/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lillipup_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/506/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_herdier_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/507/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stoutland_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/508/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_purrloin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/509/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_liepard_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/510/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pansage_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/511/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_simisage_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/512/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pansear_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/513/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_simisear_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/514/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_panpour_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/515/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_simipour_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/516/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_munna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/517/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_musharna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/518/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pidove_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/519/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tranquill_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/520/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_unfezant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/521/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_blitzle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/522/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zebstrika_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/523/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_roggenrola_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/524/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_boldore_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/525/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gigalith_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/526/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_woobat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/527/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swoobat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/528/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drilbur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/529/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_excadrill_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/530/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_audino_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/531/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_timburr_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/532/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gurdurr_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/533/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_conkeldurr_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/534/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tympole_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/535/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_palpitoad_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/536/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_seismitoad_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/537/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_throh_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/538/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sawk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/539/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sewaddle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/540/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swadloon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/541/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_leavanny_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/542/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_venipede_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/543/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_whirlipede_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/544/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scolipede_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/545/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cottonee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/546/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_whimsicott_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/547/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_petilil_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/548/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lilligant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/549/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_basculin_red_striped_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/550/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sandile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/551/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_krokorok_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/552/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_krookodile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/553/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_darumaka_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/554/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_darmanitan_standard_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/555/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_maractus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/556/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dwebble_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/557/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_crustle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/558/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scraggy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/559/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scrafty_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/560/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sigilyph_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/561/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_yamask_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/562/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cofagrigus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/563/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tirtouga_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/564/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_carracosta_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/565/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_archen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/566/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_archeops_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/567/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_trubbish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/568/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_garbodor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/569/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zorua_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/570/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zoroark_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/571/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_minccino_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/572/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cinccino_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/573/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gothita_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/574/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gothorita_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/575/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gothitelle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/576/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_solosis_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/577/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_duosion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/578/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_reuniclus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/579/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ducklett_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/580/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swanna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/581/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vanillite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/582/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vanillish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/583/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vanilluxe_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/584/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_deerling_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/585/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sawsbuck_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/586/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_emolga_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/587/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_karrablast_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/588/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_escavalier_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/589/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_foongus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/590/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_amoonguss_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/591/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_frillish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/592/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jellicent_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/593/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_alomomola_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/594/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_joltik_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/595/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_galvantula_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/596/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ferroseed_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/597/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ferrothorn_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/598/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_klink_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/599/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_klang_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/600/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_klinklang_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/601/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tynamo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/602/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_eelektrik_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/603/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_eelektross_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/604/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_elgyem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/605/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_beheeyem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/606/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_litwick_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/607/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lampent_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/608/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chandelure_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/609/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_axew_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/610/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fraxure_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/611/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_haxorus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/612/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cubchoo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/613/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_beartic_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/614/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cryogonal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/615/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shelmet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/616/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_accelgor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/617/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stunfisk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/618/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mienfoo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/619/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mienshao_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/620/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_druddigon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/621/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_golett_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/622/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_golurk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/623/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pawniard_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/624/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bisharp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/625/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bouffalant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/626/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rufflet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/627/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_braviary_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/628/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vullaby_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/629/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mandibuzz_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/630/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_heatmor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/631/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_durant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/632/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_deino_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/633/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zweilous_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/634/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hydreigon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/635/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_larvesta_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/636/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_volcarona_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/637/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cobalion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/638/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_terrakion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/639/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_virizion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/640/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tornadus_incarnate_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/641/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_thundurus_incarnate_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/642/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_reshiram_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/643/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zekrom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/644/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_landorus_incarnate_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/645/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kyurem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/646/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_keldeo_ordinary_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/647/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meloetta_aria_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/648/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_genesect_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/649/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chespin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/650/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_quilladin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/651/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chesnaught_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/652/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fennekin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/653/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_braixen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/654/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_delphox_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/655/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_froakie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/656/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_frogadier_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/657/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_greninja_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/658/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bunnelby_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/659/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_diggersby_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/660/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fletchling_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/661/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fletchinder_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/662/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_talonflame_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/663/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scatterbug_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/664/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spewpa_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/665/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vivillon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/666/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_litleo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/667/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pyroar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/668/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flabebe_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/669/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_floette_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/670/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_florges_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/671/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skiddo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/672/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gogoat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/673/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pancham_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/674/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pangoro_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/675/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_furfrou_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/676/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_espurr_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/677/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meowstic_male_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/678/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_honedge_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/679/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_doublade_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/680/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aegislash_shield_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/681/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spritzee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/682/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aromatisse_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/683/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_swirlix_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/684/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slurpuff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/685/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_inkay_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/686/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_malamar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/687/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_binacle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/688/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_barbaracle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/689/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skrelp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/690/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dragalge_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/691/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clauncher_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/692/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clawitzer_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/693/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_helioptile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/694/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_heliolisk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/695/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tyrunt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/696/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tyrantrum_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/697/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_amaura_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/698/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aurorus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/699/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sylveon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/700/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hawlucha_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/701/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dedenne_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/702/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_carbink_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/703/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_goomy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/704/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sliggoo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/705/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_goodra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/706/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_klefki_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/707/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_phantump_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/708/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_trevenant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/709/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pumpkaboo_average_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/710/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gourgeist_average_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/711/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bergmite_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/712/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_avalugg_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/713/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_noibat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/714/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_noivern_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/715/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_xerneas_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/716/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_yveltal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/717/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zygarde_50_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/718/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_diancie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/719/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hoopa_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/720/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_volcanion_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/721/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rowlet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/722/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dartrix_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/723/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_decidueye_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/724/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_litten_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/725/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_torracat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/726/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_incineroar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/727/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_popplio_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/728/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_brionne_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/729/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_primarina_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/730/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pikipek_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/731/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_trumbeak_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/732/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toucannon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/733/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_yungoos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/734/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gumshoos_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/735/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grubbin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/736/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_charjabug_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/737/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_vikavolt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/738/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_crabrawler_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/739/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_crabominable_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/740/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_oricorio_baile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/741/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cutiefly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/742/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ribombee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/743/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rockruff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/744/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lycanroc_midday_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/745/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wishiwashi_solo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/746/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mareanie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/747/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toxapex_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/748/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mudbray_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/749/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mudsdale_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/750/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dewpider_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/751/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_araquanid_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/752/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fomantis_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/753/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lurantis_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/754/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_morelull_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/755/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shiinotic_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/756/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_salandit_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/757/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_salazzle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/758/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stufful_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/759/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bewear_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/760/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bounsweet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/761/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_steenee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/762/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tsareena_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/763/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_comfey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/764/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_oranguru_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/765/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_passimian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/766/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wimpod_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/767/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_golisopod_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/768/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sandygast_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/769/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_palossand_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/770/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pyukumuku_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/771/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_type_null_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/772/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_silvally_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/773/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_minior_red_meteor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/774/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_komala_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/775/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_turtonator_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/776/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_togedemaru_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/777/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mimikyu_disguised_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/778/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bruxish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/779/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drampa_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/780/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dhelmise_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/781/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_jangmo_o_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/782/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hakamo_o_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/783/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kommo_o_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/784/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tapu_koko_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/785/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tapu_lele_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/786/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tapu_bulu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/787/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tapu_fini_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/788/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cosmog_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/789/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cosmoem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/790/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_solgaleo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/791/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lunala_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/792/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nihilego_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/793/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_buzzwole_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/794/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pheromosa_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/795/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_xurkitree_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/796/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_celesteela_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/797/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kartana_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/798/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_guzzlord_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/799/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_necrozma_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/800/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_magearna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/801/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_marshadow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/802/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_poipole_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/803/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_naganadel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/804/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stakataka_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/805/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_blacephalon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/806/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zeraora_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/807/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meltan_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/808/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_melmetal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/809/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grookey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/810/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_thwackey_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/811/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rillaboom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/812/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scorbunny_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/813/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_raboot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/814/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cinderace_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/815/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sobble_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/816/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drizzile_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/817/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_inteleon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/818/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skwovet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/819/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_greedent_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/820/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rookidee_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/821/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_corvisquire_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/822/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_corviknight_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/823/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_blipbug_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/824/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dottler_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/825/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_orbeetle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/826/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nickit_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/827/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_thievul_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/828/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gossifleur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/829/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_eldegoss_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/830/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wooloo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/831/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dubwool_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/832/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chewtle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/833/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drednaw_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/834/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_yamper_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/835/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_boltund_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/836/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rolycoly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/837/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_carkol_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/838/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_coalossal_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/839/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_applin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/840/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flapple_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/841/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_appletun_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/842/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_silicobra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/843/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sandaconda_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/844/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cramorant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/845/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arrokuda_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/846/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_barraskewda_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/847/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toxel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/848/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toxtricity_amped_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/849/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sizzlipede_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/850/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_centiskorch_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/851/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clobbopus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/852/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grapploct_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/853/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sinistea_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/854/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_polteageist_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/855/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hatenna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/856/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hattrem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/857/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_hatterene_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/858/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_impidimp_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/859/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_morgrem_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/860/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grimmsnarl_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/861/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_obstagoon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/862/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_perrserker_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/863/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cursola_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/864/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sirfetchd_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/865/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mr_rime_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/866/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_runerigus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/867/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_milcery_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/868/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_alcremie_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/869/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_falinks_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/870/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pincurchin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/871/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_snom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/872/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_frosmoth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/873/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_stonjourner_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/874/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_eiscue_ice_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/875/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_indeedee_male_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/876/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_morpeko_full_belly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/877/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cufant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/878/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_copperajah_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/879/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dracozolt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/880/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arctozolt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/881/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dracovish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/882/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arctovish_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/883/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_duraludon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/884/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dreepy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/885/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_drakloak_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/886/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dragapult_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/887/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zacian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/888/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zamazenta_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/889/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_eternatus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/890/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kubfu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/891/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_urshifu_single_strike_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/892/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_zarude_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/893/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_regieleki_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/894/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_regidrago_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/895/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_glastrier_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/896/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spectrier_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/897/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_calyrex_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/898/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wyrdeer_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/899/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kleavor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/900/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ursaluna_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/901/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_basculegion_male_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/902/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sneasler_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/903/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_overqwil_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/904/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_enamorus_incarnate_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/905/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sprigatito_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/906/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_floragato_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/907/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meowscarada_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/908/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fuecoco_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/909/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_crocalor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/910/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_skeledirge_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/911/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_quaxly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/912/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_quaxwell_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/913/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_quaquaval_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/914/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lechonk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/915/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_oinkologne_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/916/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tarountula_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/917/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_spidops_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/918/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nymble_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/919/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_lokix_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/920/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pawmi_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/921/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pawmo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/922/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pawmot_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/923/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tandemaus_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/924/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_maushold_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/925/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_fidough_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/926/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dachsbun_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/927/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_smoliv_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/928/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dolliv_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/929/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arboliva_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/930/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_squawkabilly_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/931/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_nacli_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/932/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_naclstack_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/933/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_garganacl_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/934/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_charcadet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/935/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_armarouge_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/936/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ceruledge_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/937/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tadbulb_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/938/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bellibolt_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/939/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wattrel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/940/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kilowattrel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/941/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_maschiff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/942/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_mabosstiff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/943/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shroodle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/944/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_grafaiai_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/945/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bramblin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/946/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_brambleghast_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/947/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toedscool_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/948/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_toedscruel_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/949/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_klawf_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/950/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_capsakid_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/951/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scovillain_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/952/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rellor_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/953/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rabsca_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/954/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flittle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/955/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_espathra_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/956/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tinkatink_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/957/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tinkatuff_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/958/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tinkaton_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/959/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wiglett_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/960/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wugtrio_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/961/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_bombirdier_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/962/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_finizen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/963/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_palafin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/964/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_varoom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/965/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_revavroom_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/966/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cyclizar_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/967/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_orthworm_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/968/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_glimmet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/969/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_glimmora_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/970/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_greavard_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/971/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_houndstone_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/972/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flamigo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/973/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cetoddle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/974/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_cetitan_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/975/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_veluza_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/976/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dondozo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/977/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tatsugiri_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/978/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_annihilape_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/979/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_clodsire_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/980/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_farigiraf_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/981/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_dudunsparce_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/982/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kingambit_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/983/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_great_tusk_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/984/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_scream_tail_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/985/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_brute_bonnet_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/986/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_flutter_mane_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/987/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_slither_wing_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/988/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_sandy_shocks_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/989/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_treads_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/990/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_bundle_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/991/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_hands_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/992/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_jugulis_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/993/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_moth_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/994/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_thorns_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/995/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_frigibax_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/996/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_arctibax_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/997/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_baxcalibur_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/998/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gimmighoul_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/999/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gholdengo_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1000/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wo_chien_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1001/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chien_pao_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1002/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_ting_lu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1003/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_chi_yu_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1004/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_roaring_moon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1005/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_valiant_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1006/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_koraidon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1007/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_miraidon_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1008/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_walking_wake_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1009/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_iron_leaves_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/1010/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_deoxys_attack_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10001/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_deoxys_defense_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10002/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_deoxys_speed_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10003/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wormadam_sandy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10004/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_wormadam_trash_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10005/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_shaymin_sky_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10006/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_giratina_origin_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10007/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rotom_heat_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10008/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rotom_wash_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10009/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rotom_frost_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10010/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rotom_fan_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10011/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_rotom_mow_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10012/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_castform_sunny_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10013/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_castform_rainy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10014/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_castform_snowy_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10015/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_basculin_blue_striped_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10016/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_darmanitan_zen_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10017/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meloetta_pirouette_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10018/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_tornadus_therian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10019/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_thundurus_therian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10020/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_landorus_therian_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10021/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kyurem_black_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10022/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_kyurem_white_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10023/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_keldeo_resolute_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10024/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_meowstic_female_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10025/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_aegislash_blade_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10026/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pumpkaboo_small_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10027/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pumpkaboo_large_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10028/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_pumpkaboo_super_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10029/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gourgeist_small_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10030/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gourgeist_large_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10031/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_gourgeist_super_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10032/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)


def pokemon_venusaur_mega_API(request):
    refreshme = pokedex_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = pokedex_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = pokedex_api_to_get(pokedex_api="https://pokeapi.co/api/v2/pokemon/10033/")
    savecommand.save()    
    os.system('python3 pokedexAPI.py')
    latest_answer = pokedex_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/pokedex_answer.html', latest_proposed_dict)
